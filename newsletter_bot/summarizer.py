import re
from typing import List


def simple_summary(text: str, max_sentences: int = 3) -> str:
    """Return the first few sentences of the text."""
    # split into sentences using simple regex
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    selected = sentences[:max_sentences]
    return ' '.join(s.strip() for s in selected if s)


def summarize_messages(messages: List[str]) -> str:
    summaries = [simple_summary(msg) for msg in messages]
    bullet_points = [f"- {s}" for s in summaries if s]
    return "\n".join(bullet_points)
