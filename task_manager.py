# پروژه: مدیریت وظایف روزانه
# نویسنده: امیرحسین شیری
# این خط برای گرفتن YOLO Achievement اضافه شده است
# go
# YOLO attempt — this time with a witness 😎
    
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

def list_tasks():
    if tasks:
        print("📋 لیست وظایف:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "🔲"
            print(f"{i}. {status} {task['text']}")
        print(f"🔢 تعداد کل وظایف: {len(tasks)}")
    else:
        print("هیچ وظیفه‌ای ثبت نشده.")

def show_menu():
    print("\n--- منوی مدیریت وظایف ---")
    print("1. اضافه کردن وظیفه")
    print("2. حذف وظیفه")
    print("3. نمایش وظایف")
    print("4. علامت‌گذاری وظیفه به عنوان انجام‌شده")
    print("5. خروج")

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
            print("خروج از برنامه. موفق باشی! 👋")
            break
        else:
            print("❌ گزینه نامعتبر. لطفاً دوباره تلاش کن.")
