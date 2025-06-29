from task_list import TaskList
from tasks import Task
from datetime import datetime, timedelta

def propagate_task_list(task_list: TaskList) -> TaskList:
    task_list.add_task(Task("Buy groceries", date_due = datetime.now() - timedelta(days=4)))
    task_list.add_task(Task("Do laundry", date_due = datetime.now() - timedelta(days=-2)))
    task_list.add_task(Task("Clean room", date_due = datetime.now() + timedelta(days=-1)))
    task_list.add_task(Task("Do homework", date_due = datetime.now() + timedelta(days=3)))
    task_list.add_task(Task("Walk dog", date_due = datetime.now() + timedelta(days=5)))
    task_list.add_task(Task("Do dishes", date_due = datetime.now() + timedelta(days=6)))

    return task_list


def main() -> None:
    task_list = TaskList("sanjivst")
    task_list = propagate_task_list(task_list)
    while True:
        # Display the menu options
        print("To-Do List Manager") 
        print("1. Add a task") 
        print("2. View tasks") 
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Edit the task")
        print("6. View overdue tasks")
        print("7. Quit")  
            
        choice = input("Enter your choice: ") 
            
        if choice == "1":
            title = input("Enter a task: ")
            input_date = input("Enter a due date (YYYY-MM-DD)")
            date_object = datetime.strptime(input_date, "%Y-%m-%d")
            task = Task(title, completed=False, date_due=date_object)
            task_list.add_task(task)

        elif choice == "2":
            task_list.view_tasks()

        elif choice == "3":
            ix = int(input("Enter the index of the task to remove: "))
            task_list.remove_task(ix)
            
        elif choice == "4":
            ix = int(input("Enter the index of the task to mark as completed: "))
            if 0 <= ix < len(task_list.tasks):
                task_list.tasks[ix].mark_completed()
                print(f"Task '{task_list.tasks[ix].title}' marked as completed.")
            else:
                print("Invalid index.")

        elif choice == "5":
            ix = int(input("Enter the index of the task to edit: "))
            if 0 <= ix < len(task_list.tasks):
                print("1. Change title")
                print("2. Change due date")
                print("3. Change description")
                edit_choice = input("Enter your choice: ")
                if edit_choice == "1":
                    new_title = input("Enter the new title: ")
                    task_list.tasks[ix].change_title(new_title)
                    print(f"Task title changed to '{new_title}'.")
                elif edit_choice == "2":
                    new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
                    date_object = datetime.strptime(new_due_date, "%Y-%m-%d")
                    task_list.tasks[ix].change_date_due(date_object)
                    print(f"Task due date changed to '{new_due_date}'.")
                elif edit_choice == "3":
                    new_description = input("Enter the new description: ")
                    task_list.tasks[ix].change_description(new_description)
                    print("Task description changed.")
                else:
                    print("Invalid edit option.")
            else:
                print("Invalid index.")
        elif choice == "6":
            print("Overdue tasks:")
            task_list.view_overdue_tasks()
        elif choice == "7":
            break


if __name__ == "__main__":
    main()