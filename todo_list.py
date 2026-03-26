# todo_list.py

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")


def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f"Removed: {removed}")
    except:
        print("Invalid selection.")


def main():
    while True:
        print("\nOptions: view, add, remove, quit")
        choice = input("Choose an option: ").lower()

        if choice == "view":
            show_tasks()
        elif choice == "add":
            add_task()
        elif choice == "remove":
            remove_task()
        elif choice == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
