import unittest, datetime as _dt
from task_system.observer import TaskNotifier
from task_system.models import Task

class TestObserver(unittest.TestCase):
    def test_update_prints(self):
        tn = TaskNotifier()
        t = Task("Demo", _dt.date.today(), "Cat", "low")
        t.complete()
        # just ensure no exception:
        tn.update(t)

    def test_multiple_updates(self):
        tn = TaskNotifier()
        t = Task("Task", _dt.date.today(), "Cat", "low")
        for _ in range(3):
            tn.update(t)               # idempotent side-effect allowed