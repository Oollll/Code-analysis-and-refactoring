import unittest
import datetime
from task_system.facade import TaskSystem

class TestFlow(unittest.TestCase):
    def test_full(self):
        ts = TaskSystem()
        ts.create_task("One", datetime.date.today(), "General", "low")
        ts.complete_task("One")
        task = ts._manager._tasks["One"]
        self.assertTrue(task.completed)