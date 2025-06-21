class TaskList:
    def __init__(self, owner):
        self.owner = owner.upper()
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, ix):
        try:
            del self.tasks[ix]
            print(f"Task at index {ix} removed successfully.")
        except IndexError:
            print(f"No task found at index {ix}. Please enter a valid index.")

    def view_tasks(self): 
    # TODO: Add code here to view all tasks in the list 
        for ix, task in enumerate(self.tasks):
            print(ix, task)

    def list_options(self):
        while True: 
            print("To-Do List Manager") 
            print("1. Add a task") 
            print("2. View tasks") 
            print("3. Remove a task")
            print("4. Change Title of Task")
            print("5. Mark Task as Completed")
            print("6. Quit") 
             
            choice = input("Enter your choice: ") 
             
            if choice == "1":
                title = input("Enter a task: ")
                task = Task(title) 
                self.add_task(task)

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                ix = int(input("Enter the index of the task to remove: "))
                self.remove_task(ix)
        
            elif choice == "4":
                break
        
class Task:
    def __init__(self, title, completed):
        self.title = title
        self.completed = bool(completed)

    def __str__(self):
        return f"Task: {self.title}"   
        return f"Task: {self.completed}"
    
    def mark_completed():
        Task.self.completed = True
    
    def change_title(new_title):
        Task.self.title =  new_title

my_task_list = TaskList("Sanjiv")
# This part is just to test the functionality by adding some tasks to the list
my_task_list.tasks = [Task("Do Homework"), Task("Do Laundry"), Task("Go Shopping")]
my_task_list.list_options()



