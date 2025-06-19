class TaskList:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = []
my_task_list = TaskList("John")
print(my_task_list.owner)
