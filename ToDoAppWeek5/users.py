class User:
    """Represents a generic user."""
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"User: {self.name}"

class Owner(User):
    """Represents the owner of a task list."""
    def __str__(self) -> str:
        return f"Owner: {self.name}"