import os
import imaplib
import email
from datetime import datetime, timedelta
from typing import List


def connect_imap():
    host = os.environ.get("IMAP_SERVER")
    username = os.environ.get("IMAP_USER")
    password = os.environ.get("IMAP_PASSWORD")
    port = int(os.environ.get("IMAP_PORT", "993"))
    if not all([host, username, password]):
        raise RuntimeError("IMAP credentials not fully specified in environment variables")
    mail = imaplib.IMAP4_SSL(host, port)
    mail.login(username, password)
    return mail


def fetch_newsletters(days: int = 7, sender_filter: str | None = None) -> List[str]:
    mail = connect_imap()
    mail.select("inbox")
    since_date = (datetime.utcnow() - timedelta(days=days)).strftime("%d-%b-%Y")
    search_criteria = [f'SINCE {since_date}']
    if sender_filter:
        search_criteria.append(f'FROM "{sender_filter}"')
    result, data = mail.search(None, *search_criteria)
    if result != 'OK':
        return []
    messages = []
    for num in data[0].split():
        res, msg_data = mail.fetch(num, '(RFC822)')
        if res != 'OK':
            continue
        msg = email.message_from_bytes(msg_data[0][1])
        # extract plain text
        body = []
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == 'text/plain':
                    charset = part.get_content_charset() or 'utf-8'
                    body.append(part.get_payload(decode=True).decode(charset, errors='ignore'))
        else:
            charset = msg.get_content_charset() or 'utf-8'
            body.append(msg.get_payload(decode=True).decode(charset, errors='ignore'))
        messages.append('\n'.join(body))
    mail.logout()
    return messages
