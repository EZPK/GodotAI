"""Simple context manager using in-memory storage."""

from collections import defaultdict
from typing import List


class EmbeddingContext:
    """Store recent messages for each session."""

    def __init__(self, max_messages: int = 10) -> None:
        self.max_messages = max_messages
        self._data: dict[int, List[str]] = defaultdict(list)

    def add_message(self, session_id: int, text: str) -> None:
        msgs = self._data[session_id]
        msgs.append(text)
        if len(msgs) > self.max_messages:
            del msgs[0]

    def get_recent_context(self, session_id: int, count: int = 5) -> str:
        msgs = self._data.get(session_id, [])
        return "\n".join(msgs[-count:])
