from app.models.priorita import Priorita


def filtra_per_priorita(tasks: list[dict], priorita: Priorita) -> list[dict]:
    return [
        task
        for task in tasks
        if task.get("priorita") == priorita.value
    ]