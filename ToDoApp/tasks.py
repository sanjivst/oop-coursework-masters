from datetime import datetime

class Task:
    """Represents a task in the to-do list."""
    
    def __init__(
            self, 
            title: str, 
            completed: bool = False,
            date_due: datetime = None,
            description: str = None
    ) -> None:
        self.title: str = title
        self.completed: bool = completed
        self.date_created: datetime = datetime.now()
        self.date_due: datetime = date_due
        self.description: str = description

    def __str__(self) -> str:
        return f"Task: {self.title} | Completed: {self.completed} | Description: {self.description}"          
        
    def mark_completed(self) -> None:
        """Mark the task as completed."""
        self.completed = True
    
    def change_title(self, new_title: str) -> None:
        """Changes the title of the task.

        Args:
            new_title (str): The new title for the task.
        """
        self.title =  new_title

    def change_date_due(self, date_due: datetime) -> None:
        """Changes the due date of the task.
        Args:
            date_due (datetime): The new due date for the task.
        """
        self.date_due = date_due

    def change_description(self, description: str) -> None:
        """Changes the description of the task.
        
        Args:
            description (str): The new description for the task.
        """
        self.description = description   