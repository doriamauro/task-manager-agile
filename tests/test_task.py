import pytest
from pydantic import ValidationError

from app.models.task import Task


def test_task_creation():
    task = Task(
        id=1,
        title="Prepare release",
        description="Review and publish the release.",
        completed=True,
    )

    assert task.id == 1
    assert task.title == "Prepare release"
    assert task.description == "Review and publish the release."
    assert task.completed is True


def test_task_completed_defaults_to_false():
    task = Task(
        id=1,
        title="Prepare release",
        description="Review and publish the release.",
    )

    assert task.completed is False


@pytest.mark.parametrize("missing_field", ["id", "title", "description"])
def test_task_requires_id_title_and_description(missing_field):
    task_data = {
        "id": 1,
        "title": "Prepare release",
        "description": "Review and publish the release.",
    }
    del task_data[missing_field]

    with pytest.raises(ValidationError):
        Task(**task_data)


def test_task_rejects_invalid_completed_value():
    with pytest.raises(ValidationError):
        Task(
            id=1,
            title="Prepare release",
            description="Review and publish the release.",
            completed="not-a-boolean",
        )
