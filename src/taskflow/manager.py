class TaskManager:
    def __init__(self):
        self.tasks: list[str] = []

    def add_task(self, description: str) -> None:
        description = description.strip()

        if not description:
            raise ValueError("Tasks cannot be empty.")

        self._tasks.append(description)

    def list_tasks(self) -> tuple[str, ...]:
        return  tuple(self._tasks)
