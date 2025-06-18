# Newsletter Bot

This repository includes a simple Python script that fetches emails from an IMAP inbox, summarises them and posts the summary to Slack.

## Setup

1. Set the following environment variables:
   - `IMAP_SERVER` – address of the IMAP server (e.g. `imap.gmail.com`).
   - `IMAP_PORT` – IMAP port, defaults to `993` if not provided.
   - `IMAP_USER` – username for the mailbox.
   - `IMAP_PASSWORD` – password for the mailbox.
   - `SLACK_WEBHOOK_URL` – Slack incoming webhook URL where summaries will be posted.
   - `NEWSLETTER_SENDER` – optional filter for the sender email address of newsletters.

2. Run the bot:

```bash
python -m newsletter_bot.main
```

The bot fetches emails from the last seven days, summarises them and posts the summaries to Slack. You can schedule this command with `cron` or any task scheduler to run weekly.
