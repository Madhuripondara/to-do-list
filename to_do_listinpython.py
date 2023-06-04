#to do list
def fun():
    tasks = []
    def add_task():
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully!")
    def display_tasks():
        if not tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
    def remove_task():
        display_tasks()
        if tasks:
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid task index.")
        else:
            print("No tasks found.")
    def clear_tasks():
        tasks.clear()
        print("All tasks cleared!")
    while True:
        print("\n==== TO-DO LIST ====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Remove Task")
        print("4. Clear All Tasks")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            clear_tasks()
        elif choice == "5":
            print("Thank you for using the to-do list!")
            break
        else:
            print("Invalid choice. Please try again.")
fun()
ask=input("do u want to make another to_do_list(yes/no):")
while ask=="yes":
    fun()
    ask=input("do u want to make another to_do_list(yes/no):")
else:
    print("thankyou")
    



