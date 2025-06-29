from tasks import Task
from datetime import datetime

class TaskList:
    """Represents a list of tasks for a specific user."""
    def __init__(self, owner: str) -> None:
        self.owner: str = owner.upper()
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        """Adds a task to the task list.
        Args:
            task (Task): The task to be added.
        """
        self.tasks.append(task)

    def remove_task(self, ix: int) -> None:
        """Removes a task from the task list by index.
        Args:
            ix (int): The index of the task to be removed.
        """   
        try:
            del self.tasks[ix]
            print(f"Task at index {ix} removed successfully.")
        except IndexError:
            print(f"No task found at index {ix}. Please enter a valid index.")

    def view_tasks(self) -> None: 
        """Displays all tasks in the task list with their indices."""
        for ix, task in enumerate(self.tasks):
            print(ix, task)

    def view_overdue_tasks(self) -> None: 
        """Displays all overdue tasks in the task list."""
        for ix, task in enumerate(self.tasks):
            if task.date_due and task.date_due < datetime.now():
                print(ix, task)