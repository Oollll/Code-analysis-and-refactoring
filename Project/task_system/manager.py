"""Subject + business logic that manages tasks."""
from __future__ import annotations
from typing import Dict, List
from .observer import Observer, TaskNotifier
from .models import Task

class Subject:
    """Implements basic observer registry."""
    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notify(self, task: Task) -> None:
        for ob in self._observers:
            ob.update(task)

class TaskManager(Subject):
    """Stores tasks & triggers notifications."""
    def __init__(self) -> None:
        super().__init__()
        self._tasks: Dict[str, Task] = {}

    # ---- CRUD ----
    def add_task(self, task: Task) -> None:
        self._tasks[task.title] = task

    def complete_task(self, title: str) -> None:
        if title in self._tasks:
            task = self._tasks[title]
            if not task.completed:
                task.complete()
                self.notify(task)

    # ---- Queries ----
    def all_tasks(self) -> List[Task]:
        return list(self._tasks.values())