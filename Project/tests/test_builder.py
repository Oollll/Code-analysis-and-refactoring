import unittest, datetime as _dt
from task_system.builder import TaskBuilder

class TestBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = TaskBuilder()

    def test_title(self):
        task = self.builder.set_title("T").build()
        self.assertEqual(task.title, "T")

    def test_due_date(self):
        d = _dt.date(2025, 5, 30)
        task = self.builder.set_due_date(d).build()
        self.assertEqual(task.due_date, d)

    def test_priority_default(self):
        task = self.builder.set_title("x").build()
        self.assertEqual(task.priority, "medium")

    def test_reset(self):
        self.builder.set_title("A").build()
        task2 = self.builder.set_title("B").build()
        self.assertEqual(task2.title, "B")

    # ── НОВІ ТЕСТИ ──────────────────────────────────────────────────────
    def test_builder_priority_chain(self):
        """Builder повертається в початковий стан після ланцюжка."""
        task1 = (
            self.builder
            .set_title("P1")
            .set_priority("high")
            .build()
        )
        task2 = self.builder.set_title("P2").build()
        # після reset пріоритет має бути дефолтним
        self.assertEqual(task2.priority, "medium")
        self.assertNotEqual(task1.priority, task2.priority)

    def test_builder_invalid_priority(self):
        """Edge-case: зберігається нестандартний пріоритет."""
        t = (
            self.builder
            .set_title("Edge")
            .set_priority("unknown")
            .build()
        )
        self.assertEqual(t.priority, "unknown")