def add_task():
    task = input("Enter a task : ")
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print("Task added succssfully !!! \n")

def show_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()

        if(len(tasks) == 0):
            print("To-Do list is Empty !!")
            return
        
        print("==== Your To-Do List ====")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")
    
    except FileNotFoundError:
        print("No Tasks Available !")

def delete_tasks():
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()

    if(len(tasks) == 0):
        print("No Tasks !! Nothing to Delete !!")
        return
    
    show_tasks()
    try:
        user_choice = int(input("Enter number of task which you want to delete :"))
    except ValueError:
        print("Please enter a valid number!")
        return
    
    if(user_choice <= 0 or user_choice > len(tasks)):
        print("Enter a valid choice !")
        return
    
    index = user_choice - 1
    deleted_task= tasks.pop(index)
    with open("tasks.txt", "w") as f:
        f.writelines(tasks)
    print(f"Deleted : {deleted_task}")

    print("Task deleted successfully !")

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

    else:
        print("Invalid Option !!")