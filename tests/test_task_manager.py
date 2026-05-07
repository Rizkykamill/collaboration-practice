import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.task_manager import (
    get_all_tasks,
    add_task
)

from src.task_manager import (
    get_all_tasks,
    add_task
)

def sample_tasks():
    return [
        {
            "id": 1,
            "title": "Test",
            "description": "Testing",
            "status": "todo",
            "priority": "high",
            "assignee": "Rina"
        }
    ]

def test_get_all_tasks():
    tasks = sample_tasks()
    result = get_all_tasks(tasks)
    assert len(result) == 1

def test_add_task():
    tasks = sample_tasks()

    result = add_task(
        tasks,
        "Login",
        "Testing login",
        "high",
        "Sari"
    )

    assert len(result) == 5