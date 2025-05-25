"""Domain entity."""
from __future__ import annotations
import datetime as _dt

class Task:
    """Immutable-style task entity (state changes тільки через complete)."""
    def __init__(self, title: str, due_date: _dt.date,
                 category: str, priority: str) -> None:
        self.title: str      = title
        self.due_date: _dt.date = due_date
        self.category: str   = category
        self.priority: str   = priority
        self.completed: bool = False

    def complete(self) -> None:
        """Mark task as done (idempotent)."""
        self.completed = True