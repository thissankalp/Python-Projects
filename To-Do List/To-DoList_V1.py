tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)

def show_tasks():
    if len(tasks) == 0:
        print("No tasks available!")
        return

def delete_tasks():
    if(len(tasks) == 0):
        print("No Tasks !! Nothing to Delete !!")
        return
    
    user_choice = int(input("Enter number of task which you want to delete :"))
    show_tasks()
    if(user_choice <= 0 or user_choice > len(tasks)):
        print("Enter a valid choice !")
        return
    
    index = user_choice - 1
    deleted_task= tasks.pop(index)
    print(f"Deleted : {deleted_task}")

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Show Tasks")
    print("4. Exit")

    try:
        option = int(input("Choose option: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if option == 1:
        add_task()

    elif option == 2:
        delete_tasks()

    elif option == 3:
        show_tasks()

    elif option == 4:
        break