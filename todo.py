def load_tasks():
    try:
        with open('tasks.txt', 'r') as f:
            tasks = f.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open('tasks.txt', 'w') as f:
        for task in tasks:
            f.write(task + '\n')


def add_task(task, tasks):
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def delete_task(task_index, tasks):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")


def mark_task_completed(task_index, tasks):
    if 0 <= task_index < len(tasks):
        tasks[task_index] += ' - Completed'
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

def display_tasks(tasks):
    if tasks:
        print("Your To-Do List:")

        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")
    else:
        print("Your To-Do List is empty!")


def main():
    print("Welcome to To-Do List App!")
    tasks = load_tasks()


    while True:
        print("\nOptions:")

        print("1. Add Task")

        print("2. Delete Task")

        print("3. Mark Task as Completed")
        print("4. View Tasks")

        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task, tasks)

        elif choice == '2':
            display_tasks(tasks)
            task_index = int(input("Enter the index of the task to delete: ")) - 1
            delete_task(task_index, tasks)

        elif choice == '3':
            display_tasks(tasks)
            task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
            mark_task_completed(task_index, tasks)
        elif choice == '4':
            display_tasks(tasks)

        elif choice == '5':
            print("Thank you for using To-Do List App!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




