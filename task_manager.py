# پروژه: مدیریت وظایف روزانه
# نویسنده: امیرحسین شیری

tasks = []

def add_task(task):
    if task in tasks:
        print(f"⚠️ وظیفه '{task}' قبلاً اضافه شده.")
    else:
        tasks.append(task)
        print(f"✅ وظیفه '{task}' اضافه شد.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"🗑️ وظیفه '{task}' حذف شد.")
    else:
        print(f"⚠️ وظیفه '{task}' پیدا نشد.")

def list_tasks():
    if tasks:
        print("📋 لیست وظایف:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print(f"🔢 تعداد کل وظایف: {len(tasks)}")
    else:
        print("هیچ وظیفه‌ای ثبت نشده.")

def show_menu():
    print("\n--- منوی مدیریت وظایف ---")
    print("1. اضافه کردن وظیفه")
    print("2. حذف وظیفه")
    print("3. نمایش وظایف")
    print("4. خروج")

def welcome():
    print("👋 خوش آمدی به برنامه مدیریت وظایف روزانه!")
    print("✨ با این ابزار ساده می‌تونی وظایف‌ت رو بهتر مدیریت کنی.")

if __name__ == "__main__":
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
            print("خروج از برنامه. موفق باشی! 👋")
            break
        else:
            print("❌ گزینه نامعتبر. لطفاً دوباره تلاش کن.")
