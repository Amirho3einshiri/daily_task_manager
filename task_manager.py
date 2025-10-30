tasks = []

FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("||")
                if len(parts) == 2:
                    task, status = parts
                    tasks.append({"text": task, "done": status == "done"})
        print(f"📦 {len(tasks)} وظیفه بارگذاری شد.")
    except FileNotFoundError:
        pass

def save_tasks():
    with open(FILENAME, "w", encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "todo"
            f.write(f"{task['text']}||{status}\n")

def add_task(task_text):
    for task in tasks:
        if task["text"] == task_text:
            print(f"⚠️ وظیفه '{task_text}' قبلاً اضافه شده.")
            return
    tasks.append({"text": task_text, "done": False})
    print(f"✅ وظیفه '{task_text}' اضافه شد.")
    save_tasks()

def remove_task(task_text):
    for task in tasks:
        if task["text"] == task_text:
            tasks.remove(task)
            print(f"🗑️ وظیفه '{task_text}' حذف شد.")
            save_tasks()
            return
    print(f"⚠️ وظیفه '{task_text}' پیدا نشد.")

def mark_done(task_text):
    for task in tasks:
        if task["text"] == task_text:
            task["done"] = True
            print(f"✅ وظیفه '{task_text}' به عنوان انجام‌شده علامت‌گذاری شد.")
            save_tasks()
            return
    print(f"⚠️ وظیفه '{task_text}' پیدا نشد.")

def edit_task(old_text, new_text):
    for task in tasks:
        if task["text"] == old_text:
            task["text"] = new_text
            print(f"✏️ وظیفه '{old_text}' به '{new_text}' تغییر یافت.")
            save_tasks()
            return
    print(f"⚠️ وظیفه '{old_text}' پیدا نشد.")

def list_tasks():
    if tasks:
        print("📋 لیست وظایف:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "🔲"
            print(f"{i}. {status} {task['text']}")
        print(f"🔢 تعداد کل وظایف: {len(tasks)}")
    else:
        print("هیچ وظیفه‌ای ثبت نشده.")

def list_pending_tasks():
    pending = [task for task in tasks if not task["done"]]
    if pending:
        print("🔲 وظایف انجام‌نشده:")
        for i, task in enumerate(pending, 1):
            print(f"{i}. {task['text']}")
        print(f"📌 تعداد وظایف انجام‌نشده: {len(pending)}")
    else:
        print("🎉 همه وظایف انجام شده!")

def list_done_tasks():
    done = [task for task in tasks if task["done"]]
    if done:
        print("✅ وظایف انجام‌شده:")
        for i, task in enumerate(done, 1):
            print(f"{i}. {task['text']}")
        print(f"📌 تعداد وظایف انجام‌شده: {len(done)}")
    else:
        print("⏳ هنوز هیچ وظیفه‌ای انجام نشده.")

def show_menu():
    print("\n--- منوی مدیریت وظایف ---")
    print("1. اضافه کردن وظیفه")
    print("2. حذف وظیفه")
    print("3. نمایش وظایف")
    print("4. علامت‌گذاری وظیفه به عنوان انجام‌شده")
    print("5. ویرایش متن وظیفه")
    print("6. خروج")
    print("7. نمایش فقط وظایف انجام‌نشده")
    print("8. نمایش فقط وظایف انجام‌شده")  # گزینه جدید

def welcome():
    print("👋 خوش آمدی به برنامه مدیریت وظایف روزانه!")
    print("✨ با این ابزار ساده می‌تونی وظایف‌ت رو بهتر مدیریت کنی.")

if __name__ == "__main__":
    load_tasks()
    welcome()
    while True:
        show_menu()
        choice = input("انتخاب شما: ")

        if choice == "1":
            task = input("متن وظیفه: ")
            add_task(task)
        elif choice == "2":
            task = input("وظیفه‌ای که می‌خوای حذف کنی: ")
            remove_task(task)
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            task = input("وظیفه‌ای که انجام شده: ")
            mark_done(task)
        elif choice == "5":
            old_text = input("متن فعلی وظیفه: ")
            new_text = input("متن جدید وظیفه: ")
            edit_task(old_text, new_text)
        elif choice == "6":
            print("خروج از برنامه. موفق باشی! 👋")
            break
        elif choice == "7":
            list_pending_tasks()
        elif choice == "8":
            list_done_tasks()
        else:
            print("❌ گزینه نامعتبر. لطفاً دوباره تلاش کن.")
