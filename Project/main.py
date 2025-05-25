"""Entry point that demonstrates Facade usage."""
from task_system.facade import TaskSystem
import datetime as _dt

def main() -> None:
    ts = TaskSystem()

    ts.create_task("Завершити лабу", _dt.date(2025, 5, 30), "Навчання", "high")
    ts.create_task("Зробити бекап",   _dt.date(2025, 5, 28), "DevOps",    "medium")

    ts.show_tasks()          # до завершення
    ts.complete_task("Завершити лабу")
    ts.show_tasks()          # після завершення

if __name__ == "__main__":
    main()