"""Builder pattern — step-by-step Task creation."""
from __future__ import annotations
import datetime as _dt
from .models import Task

class TaskBuilder:
    """Fluent builder for Task objects."""
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._title: str = ""
        self._due_date: _dt.date = _dt.date.today()
        self._category: str = ""
        self._priority: str = "medium"

    def set_title(self, title: str) -> "TaskBuilder":
        self._title = title
        return self

    def set_due_date(self, due_date: _dt.date) -> "TaskBuilder":
        self._due_date = due_date
        return self

    def set_category(self, category: str) -> "TaskBuilder":
        self._category = category
        return self

    def set_priority(self, priority: str) -> "TaskBuilder":
        self._priority = priority
        return self

    def build(self) -> Task:
        """Return new Task and reset builder."""
        task = Task(self._title, self._due_date, self._category, self._priority)
        self.reset()
        return task