tasks = []


def show_menu():
    print("\n==== To-Do List Menu ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    
    
def view_tasks():
    if not tasks:
        print("No tasks added yet.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

            
def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!")
    
    
def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f"Removed: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number.")
        
        
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            

if __name__ == "__main__":
    main()
