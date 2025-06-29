from datetime import datetime


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
        for ix, task in enumerate(self.tasks):
            print(ix, task)

    def list_options(self):
        while True: 
            print("To-Do List Manager") 
            print("1. Add a task") 
            print("2. View tasks") 
            print("3. Remove a task")
            print("4. Mark a task as completed")
            print("5. Edit the task")
            print("6. Quit")  
             
            choice = input("Enter your choice: ") 
             
            if choice == "1":
                title = input("Enter a task: ")
                input_date = input("Enter a due date (YYYY-MM-DD)")
                date_object = datetime.strptime(input_date, "%Y-%m-%d")
                task = Task(title, completed=False, date_due=date_object) 
                self.add_task(task)

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                ix = int(input("Enter the index of the task to remove: "))
                self.remove_task(ix)
                
            elif choice == "4":
                ix = int(input("Enter the index of the task to mark as completed: "))
                if 0 <= ix < len(self.tasks):
                    self.tasks[ix].mark_completed()
                    print(f"Task '{self.tasks[ix].title}' marked as completed.")
                else:
                    print("Invalid index.")

            elif choice == "5":
                ix = int(input("Enter the index of the task to edit: "))
                if 0 <= ix < len(self.tasks):
                    print("1. Change title")
                    print("2. Change due date")
                    edit_choice = input("Enter your choice: ")
                    if edit_choice == "1":
                        new_title = input("Enter the new title: ")
                        self.tasks[ix].change_title(new_title)
                        print(f"Task title changed to '{new_title}'.")
                    elif edit_choice == "2":
                        new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
                        date_object = datetime.strptime(new_due_date, "%Y-%m-%d")
                        self.tasks[ix].change_date_due(date_object)
                        print(f"Task due date changed to '{new_due_date}'.")
                    else:
                        print("Invalid edit option.")
                else:
                    print("Invalid index.")


            elif choice == "6":
                break
        
class Task:
    def __init__(self, title, completed=False, date_due=None):
        self.title = title
        self.completed = bool(completed)
        self.date_created = datetime.now()
        self.date_due = date_due

    def __str__(self):
        return f"Task: {self.title} | Completed: {self.completed}"          
        
    def mark_completed(self):
        self.completed = True
    
    def change_title(self, new_title):
        self.title =  new_title

    def change_date_due(self, date_due):
        self.date_due = date_due

my_task_list = TaskList("Sanjiv")
my_task_list.tasks = [Task("Do Homework"), Task("Do Laundry"), Task("Go Shopping"), Task("Clean Room"), Task("Work on Assignment")]
my_task_list.list_options()



