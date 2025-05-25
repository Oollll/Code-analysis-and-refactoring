"""Facade exposing simple high-level API."""
from __future__ import annotations
from typing import List
import datetime as _dt
from .builder import TaskBuilder
from .manager import TaskManager
from .observer import TaskNotifier
from .models import Task

class TaskSystem:
    """High-level façade that hides internal complexity."""
    def __init__(self) -> None:
        self._builder = TaskBuilder()
        self._manager = TaskManager()
        self._manager.attach(TaskNotifier())

    # ---- API ----
    def create_task(self, title: str, due_date: _dt.date,
                    category: str, priority: str = "medium") -> None:
        task = (
            self._builder.set_title(title)
            .set_due_date(due_date)
            .set_category(category)
            .set_priority(priority)
            .build()
        )
        self._manager.add_task(task)

    def complete_task(self, title: str) -> None:
        self._manager.complete_task(title)

    def show_tasks(self) -> None:
        for t in self.tasks():
            status = "✅" if t.completed else "❌"
            print(f"{t.title:20} | {t.due_date} | {t.category:10} | "
                  f"{t.priority.upper():6} | {status}")

    # ---- Exposed read-only data ----
    def tasks(self) -> List[Task]:
        return self._manager.all_tasks()