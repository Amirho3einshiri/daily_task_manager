"""
A simple command-line task management application (To-Do List).
Tasks are persisted in a text file with format: task_text||status
"""

from pathlib import Path

FILENAME = Path("tasks.txt")
tasks = []


def load_tasks() -> None:
    """Load tasks from the file into memory."""
    if not FILENAME.exists():
        return

    try:
        with FILENAME.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("||")
                if len(parts) == 2:
                    task_text, status = parts
                    tasks.append({"text": task_text, "done": status == "done"})
        print(f"📦 Loaded {len(tasks)} task(s).")
    except Exception as e:
        print(f"⚠️ Error loading tasks: {e}")


def save_tasks() -> None:
    """Save current tasks to the file."""
    try:
        with FILENAME.open("w", encoding="utf-8") as f:
            for task in tasks:
                status = "done" if task["done"] else "todo"
                f.write(f"{task['text']}||{status}\n")
    except Exception as e:
        print(f"⚠️ Error saving tasks: {e}")


def find_task(task_text: str):
    """Find a task by exact text match (case-sensitive). Returns task dict or None."""
    task_text = task_text.strip()
    for task in tasks:
        if task["text"] == task_text:
            return task
    return None


def add_task(task_text: str) -> None:
    """Add a new task if it doesn't already exist."""
    task_text = task_text.strip()
    if not task_text:
        print("⚠️ Task text cannot be empty.")
        return

    if find_task(task_text):
        print(f"⚠️ Task '{task_text}' already exists.")
        return

    tasks.append({"text": task_text, "done": False})
    print(f"✅ Task '{task_text}' added.")
    save_tasks()


def remove_task(task_text: str) -> None:
    """Remove a task by exact text."""
    task = find_task(task_text)
    if task:
        tasks.remove(task)
        print(f"🗑️ Task '{task_text}' removed.")
        save_tasks()
    else:
        print(f"⚠️ Task '{task_text}' not found.")


def mark_done(task_text: str) -> None:
    """Mark a task as completed."""
    task = find_task(task_text)
    if task:
        task["done"] = True
        print(f"✅ Task '{task_text}' marked as done.")
        save_tasks()
    else:
        print(f"⚠️ Task '{task_text}' not found.")


def edit_task(old_text: str, new_text: str) -> None:
    """Edit the text of an existing task."""
    old_text = old_text.strip()
    new_text = new_text.strip()
    if not new_text:
        print("⚠️ New task text cannot be empty.")
        return

    task = find_task(old_text)
    if task:
        task["text"] = new_text
        print(f"✏️ Task '{old_text}' updated to '{new_text}'.")
        save_tasks()
    else:
        print(f"⚠️ Task '{old_text}' not found.")


def list_tasks() -> None:
    """Display all tasks."""
    if not tasks:
        print("No tasks registered yet.")
        return

    print("📋 All Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "🔲"
        print(f"{i}. {status} {task['text']}")
    print(f"🔢 Total tasks: {len(tasks)}")


def list_pending_tasks() -> None:
    """Display only pending tasks."""
    pending = [t for t in tasks if not t["done"]]
    if pending:
        print("🔲 Pending Tasks:")
        for i, task in enumerate(pending, 1):
            print(f"{i}. {task['text']}")
        print(f"📌 Count: {len(pending)}")
    else:
        print("🎉 All tasks completed!")


def list_done_tasks() -> None:
    """Display only completed tasks."""
    done = [t for t in tasks if t["done"]]
    if done:
        print("✅ Completed Tasks:")
        for i, task in enumerate(done, 1):
            print(f"{i}. {task['text']}")
        print(f"📌 Count: {len(done)}")
    else:
        print("⏳ No tasks completed yet.")


def search_tasks(keyword: str) -> None:
    """Search tasks containing the keyword (case-insensitive)."""
    keyword = keyword.strip().lower()
    if not keyword:
        print("⚠️ Search keyword cannot be empty.")
        return

    results = [t for t in tasks if keyword in t["text"].lower()]
    if results:
        print(f"🔍 Search results for '{keyword}':")
        for i, task in enumerate(results, 1):
            status = "✅" if task["done"] else "🔲"
            print(f"{i}. {status} {task['text']}")
        print(f"📌 Found: {len(results)} result(s)")
    else:
        print(f"❌ No tasks found containing '{keyword}'.")


def clear_done_tasks() -> None:
    """Remove all completed tasks."""
    global tasks
    done_count = sum(1 for t in tasks if t["done"])
    if done_count == 0:
        print("No completed tasks to clear.")
        return

    tasks = [t for t in tasks if not t["done"]]
    save_tasks()
    print(f"🧹 Cleared {done_count} completed task(s).")


def show_menu() -> None:
    """Display the main menu."""
    print("\n" + "="*30)
    print("   Task Manager Menu")
    print("="*30)
    print("1. Add task")
    print("2. Remove task")
    print("3. List all tasks")
    print("4. Mark task as done")
    print("5. Edit task")
    print("6. List pending tasks")
    print("7. List completed tasks")
    print("8. Search tasks")
    print("9. Clear completed tasks")
    print("10. Exit")
    print("="*30)


def main() -> None:
    """Main program loop."""
    load_tasks()
    print("👋 Welcome to the Daily Task Manager!")
    print("✨ Manage your tasks easily with this simple tool.\n")

    while True:
        show_menu()
        choice = input("\nYour choice: ").strip()

        if choice == "1":
            task = input("Enter task text: ")
            add_task(task)

        elif choice == "2":
            task = input("Enter task text to remove: ")
            remove_task(task)

        elif choice == "3":
            list_tasks()

        elif choice == "4":
            task = input("Enter completed task text: ")
            mark_done(task)

        elif choice == "5":
            old = input("Current task text: ")
            new = input("New task text: ")
            edit_task(old, new)

        elif choice == "6":
            list_pending_tasks()

        elif choice == "7":
            list_done_tasks()

        elif choice == "8":
            keyword = input("Enter search keyword: ")
            search_tasks(keyword)

        elif choice == "9":
            clear_done_tasks()

        elif choice == "10":
            print("\nGoodbye! Have a productive day! 👋\n")
            break

        else:
            print("❌ Invalid option. Please enter a number between 1 and 10.")


if __name__ == "__main__":
    main()