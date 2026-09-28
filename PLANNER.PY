"""Task operations and command-line menu for Rishab Study Planner."""


def display_tasks(tasks, include_status=True):
    """Print tasks with one-based numbers. Return whether any tasks exist."""
    if not tasks:
        print("No tasks available.")
        return False

    for number, task in enumerate(tasks, start=1):
        line = f"{number}. {task['subject']} - {task['task']}"
        if include_status:
            status = "Completed" if task["completed"] else "Pending"
            line += f" - {status}"
        print(line)
    return True


def add_task(tasks):
    """Ask for task details and add a new pending task."""
    subject = input("Enter subject: ").strip()
    description = input("Enter study task: ").strip()

    if not subject or not description:
        print("Subject and study task cannot be empty.")
        return

    tasks.append({
        "subject": subject,
        "task": description,
        "completed": False
    })
    print("Task added successfully!")


def complete_task(tasks):
    """Mark a selected task as completed."""
    if not display_tasks(tasks, include_status=False):
        return

    number = read_task_number("Enter task number to complete: ", len(tasks))
    if number is None:
        return

    tasks[number - 1]["completed"] = True
    print("Task completed successfully!")


def delete_task(tasks):
    """Delete a selected task."""
    if not display_tasks(tasks, include_status=False):
        return

    number = read_task_number("Enter task number to delete: ", len(tasks))
    if number is None:
        return

    removed = tasks.pop(number - 1)
    print(f"Task deleted successfully: {removed['task']}")


def read_task_number(prompt, task_count):
    """Read and validate a one-based task number."""
    try:
        number = int(input(prompt))
    except ValueError:
        print("Please enter a valid number.")
        return None

    if not 1 <= number <= task_count:
        print("Invalid task number.")
        return None

    return number


def run_planner():
    """Run the interactive study-planner menu."""
    tasks = []

    print("====================")
    print("RISHAB STUDY PLANNER")
    print("====================")

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            print("\nYour Study Tasks:")
            display_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thank you for using Study Planner!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")