import unittest, datetime as _dt
from unittest.mock import MagicMock
from task_system.manager import TaskManager
from task_system.models import Task
from task_system.observer import TaskNotifier

class TestManager(unittest.TestCase):
    def setUp(self):
        self.mgr = TaskManager()
        self.mgr.attach(TaskNotifier())

    def test_add(self):
        t = Task("A", _dt.date.today(), "X", "low")
        self.mgr.add_task(t)
        self.assertEqual(len(self.mgr.all_tasks()), 1)

    def test_complete_triggers(self):
        t = Task("B", _dt.date.today(), "X", "low")
        self.mgr.add_task(t)
        self.mgr.complete_task("B")
        self.assertTrue(t.completed)

    def test_complete_nonexistent(self):
        # не повинно кидати виняток
        self.mgr.complete_task("ZZ")

    def test_no_duplicate_complete(self):
        t = Task("C", _dt.date.today(), "X", "low")
        self.mgr.add_task(t)
        self.mgr.complete_task("C")
        self.mgr.complete_task("C")   # вдруге — має бути idempotent
        self.assertTrue(t.completed)

    # ── НОВІ ТЕСТИ ──────────────────────────────────────────────────────
    def test_duplicate_titles_overwrite(self):
        """Другий Task з тим же title перезаписує перший."""
        t1 = Task("Dup", _dt.date.today(), "A", "low")
        t2 = Task("Dup", _dt.date.today(), "B", "high")
        self.mgr.add_task(t1)
        self.mgr.add_task(t2)
        self.assertEqual(len(self.mgr.all_tasks()), 1)
        self.assertEqual(self.mgr.all_tasks()[0].category, "B")

    def test_notify_called_once(self):
        """Повторний complete не викликає notify двічі."""
        mock_obs = MagicMock()
        self.mgr.attach(mock_obs)
        t = Task("Once", _dt.date.today(), "Cat", "low")
        self.mgr.add_task(t)
        self.mgr.complete_task("Once")
        self.mgr.complete_task("Once")
        mock_obs.update.assert_called_once()     # саме один виклик