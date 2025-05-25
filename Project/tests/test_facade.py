import unittest, datetime as _dt
from task_system.facade import TaskSystem

class TestFacade(unittest.TestCase):
    def setUp(self):
        self.sys = TaskSystem()

    def test_create(self):
        self.sys.create_task("T", _dt.date.today(), "Cat", "high")
        self.assertEqual(len(self.sys.tasks()), 1)

    def test_complete(self):
        self.sys.create_task("X", _dt.date.today(), "Cat", "low")
        self.sys.complete_task("X")
        self.assertTrue(self.sys.tasks()[0].completed)

    def test_show(self):
        self.sys.create_task("Y", _dt.date.today(), "Cat", "low")
        self.sys.show_tasks()  # не має викликати винятків

    def test_multiple(self):
        for i in range(3):
            self.sys.create_task(f"T{i}", _dt.date.today(), "Cat", "low")
        self.assertEqual(len(self.sys.tasks()), 3)

    # ── НОВИЙ ТЕСТ ─────────────────────────────────────────────────────
    def test_complete_nonexistent(self):
        """Метод complete_task має бути безпечним для неіснуючої назви."""
        try:
            self.sys.complete_task("DoesNotExist")
        except Exception as exc:
            self.fail(f"Facade raised {exc} on absent task")