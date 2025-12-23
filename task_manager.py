from pathlib import Path
from datetime import datetime

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
                task_text = parts[0]
                status = parts[1] if len(parts) > 1 else "todo"
                due_date = parts[2] if len(parts) > 2 else None  # جدید: تاریخ سررسید
                
                tasks.append({
                    "text": task_text,
                    "done": status == "done",
                    "due_date": due_date  # می‌تونه None یا تاریخ به فرمت YYYY-MM-DD باشه
                })
        print(f"📦 Loaded {len(tasks)} task(s).")
    except Exception as e:
        print(f"⚠️ Error loading tasks: {e}")

def save_tasks() -> None:
    """Save current tasks to the file."""
    try:
        with FILENAME.open("w", encoding="utf-8") as f:
            for task in tasks:
                status = "done" if task["done"] else "todo"
                due_date = task["due_date"] if task["due_date"] else ""
                f.write(f"{task['text']}||{status}||{due_date}\n")
    except Exception as e:
        print(f"⚠️ Error saving tasks: {e}")

# بقیه توابع find_task, remove_task, mark_done, edit_task بدون تغییر می‌مونن

def add_task(task_text: str, due_date: str = None) -> None:
    """Add a new task with optional due date."""
    task_text = task_text.strip()
    if not task_text:
        print("⚠️ Task text cannot be empty.")
        return
    if find_task(task_text):
        print(f"⚠️ Task '{task_text}' already exists.")
        return
    
    # اعتبارسنجی تاریخ اگر وارد شده
    if due_date:
        due_date = due_date.strip()
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("⚠️ Invalid date format. Use YYYY-MM-DD (e.g., 2025-12-31)")
            return
    
    tasks.append({"text": task_text, "done": False, "due_date": due_date})
    due_msg = f" (due: {due_date})" if due_date else ""
    print(f"✅ Task '{task_text}' added{due_msg}.")
    save_tasks()

def list_tasks() -> None:
    """Display all tasks with due dates."""
    if not tasks:
        print("No tasks registered yet.")
        return
    print("📋 All Tasks:")
    today = datetime.now().date()
    
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "🔲"
        due = ""
        if task["due_date"]:
            try:
                due_date_obj = datetime.strptime(task["due_date"], "%Y-%m-%d").date()
                days_left = (due_date_obj - today).days
                if task["done"]:
                    due = f" (due: {task['due_date']})"
                elif days_left < 0:
                    due = f" (overdue by {-days_left} days! ⏰)"
                elif days_left == 0:
                    due = f" (due today! 🔥)"
                elif days_left == 1:
                    due = f" (due tomorrow)"
                else:
                    due = f" (due in {days_left} days)"
            except:
                due = f" (due: {task['due_date']})"
        print(f"{i}. {status} {task['text']}{due}")
    print(f"🔢 Total tasks: {len(tasks)}")

# تغییر کوچک در منو و main

def show_menu() -> None:
    print("\n" + "="*40)
    print("       Task Manager Menu (با تاریخ سررسید!)")
    print("="*40)
    print("1. Add task (with optional due date)")
    print("2. Remove task")
    print("3. List all tasks")
    print("4. Mark task as done")
    print("5. Edit task")
    print("6. List pending tasks")
    print("7. List completed tasks")
    print("8. Search tasks")
    print("9. Clear completed tasks")
    print("10. Exit")
    print("="*40)

def main() -> None:
    load_tasks()
    print("👋 Welcome to the Daily Task Manager!")
    print("✨ Now with due dates! Enter date as YYYY-MM-DD (optional)\n")

    while True:
        show_menu()
        choice = input("\nYour choice: ").strip()

        if choice == "1":
            task = input("Enter task text: ").strip()
            if not task:
                continue
            due = input("Enter due date (YYYY-MM-DD, or leave empty): ").strip()
            due = due if due else None
            add_task(task, due)

        # بقیه گزینه‌ها مثل قبل...
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