from .fetch_email import fetch_newsletters
from .summarizer import summarize_messages
from .slack_client import post_to_slack


def run(days: int = 7, sender: str | None = None) -> None:
    messages = fetch_newsletters(days=days, sender_filter=sender)
    if not messages:
        print("No newsletters found")
        return
    summary = summarize_messages(messages)
    post_to_slack(summary)


if __name__ == "__main__":
    run()
