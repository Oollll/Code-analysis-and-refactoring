"""Observer abstraction + concrete notifier."""
from __future__ import annotations
from abc import ABC, abstractmethod
from .models import Task

class Observer(ABC):
    """Observer interface."""
    @abstractmethod
    def update(self, task: Task) -> None: ...

class TaskNotifier(Observer):
    """Console notifier (could be replaced by e-mail, webhook, etc.)."""
    def update(self, task: Task) -> None:
        print(f"[NOTIFICATION] Task '{task.title}' marked as completed.")