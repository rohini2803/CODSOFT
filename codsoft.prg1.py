#To_do list in python
to_do_list = []

def display_menu():
    print("\nTo-Do List Options:")
    print("1.View Tasks")
    print("2.Add Task")
    print("3.Mark Task as finished")
    print("4.Delete Task")
    print("5.Exit")

def show_tasks():
  if not to_do_list:
     print("\n To-do list is empty!")
  else:
    print("\n Enter Tasks:")
    for index, task in enumerate(to_do_list, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{index}. {task['task']} - {status}")

def add_task():
    task = input("\nEnter the task: ")
    to_do_list.append({"task": task, "completed": False})
    print("Task added successfully")

def mark_finished():
    show_tasks()
    try:
        task_number = int(input("\nEnter the task number to mark as finished: "))
        to_do_list[task_number - 1]["completed"] = True
        print("Task marked are finished")
    except (IndexError, ValueError):
        print("Invalid task number")

def delete_task():
    show_tasks()
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        removed_task = to_do_list.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' deleted successfully")
    except (IndexError, ValueError):
        print("Invalid task number")

while True:
    display_menu()
    choice = input("\nEnter your choice:")
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_finished()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List")
        break
    else:
        print("Invalid choice") 
