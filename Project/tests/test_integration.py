import unittest, datetime as _dt
from task_system.facade import TaskSystem

class TestIntegration(unittest.TestCase):
    def test_full_flow(self):
        ts = TaskSystem()
        ts.create_task("One", _dt.date.today(), "Gen", "low")
        ts.create_task("Two", _dt.date.today(), "Gen", "medium")

        # Complete one
        ts.complete_task("One")

        done = [t for t in ts.tasks() if t.completed]
        pending = [t for t in ts.tasks() if not t.completed]

        self.assertEqual(len(done), 1)
        self.assertEqual(len(pending), 1)

    def test_order_independent(self):
        ts = TaskSystem()
        titles = ["A", "B", "C", "D"]
        for t in titles:
            ts.create_task(t, _dt.date.today(), "Cat", "low")
        self.assertCountEqual([t.title for t in ts.tasks()], titles)