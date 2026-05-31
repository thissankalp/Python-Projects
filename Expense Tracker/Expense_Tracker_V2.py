import json
expenses = []

def load_Expenses():
    global expenses
    try:
        with open("expenses.json", "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []

def save_Expenses():
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)

def add_Expense():
    category = input("Enter expenses category : ")
    try:
        amount = float(input("Enter amount : "))
    except ValueError:
        print("Please enter a valid amount!")
        return
    description = input("Enter description : ")

    expense = {
        "category" : category,
        "amount" : amount,
        "description" : description
    }
    expenses.append(expense)
    save_Expenses()
    
    print("Expense Added")

def view_Expenses():
    if(len(expenses) == 0):
        print("No expenses Available !!")
        return
    
    print("===== All Expenses =====")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Category : {expense['category']} - Amount : ₹{expense['amount']:.2f} - Description : {expense['description']}")

def total_Expense():
    if len(expenses) == 0:
        print("No expenses available!")
        return
    
    total = 0
    for expense in expenses:
        total += expense['amount']
    print(f"Total Expense : ₹{total:.2f}")

def category_Summary():
    if len(expenses) == 0:
        print("No expenses available!")
        return
    summary = {}
    for expense in expenses:
        category = expense['category']

        if category not in summary:
            summary[category] = 0
        summary[category] += expense['amount']
    
    print("\n===== Category Summary =====")
    for category, total in summary.items():
        print(f"{category} : ₹{total:.2f}")

def delete_Expense():
    if len(expenses) == 0:
        print("No expenses available !")
        return
    
    view_Expenses()

    try:
        choice = int(input("Enter the expenses you want to delete : "))
    except ValueError:
        print("Invalid input !")
        return
    
    if choice <= 1 or choice > len(expenses):
        print("Invalid Choice !!")
        return 
    deleted_Expense = expenses.pop(choice - 1)
    save_Expenses()

    print(f"Expense Deleted : {deleted_Expense['category']}")

def filter_By_Category():
    category = input("Enter Category : ")
    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(
                f"{expense['category']} - "
                f"₹{expense['amount']:.2f} - "
                f"{expense['description']}"
            )

            found = True
        
    if not found:
        print("No Expense Found !!")

load_Expenses()
while True:
    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Summary")
    print("5. Delete Expense")
    print("6. Filter Expenses By Category")
    print("7. Exit")

    try:
        option = int(input("Select One option : "))
    except ValueError:
        print("Please enter a valid option!")
        continue

    if option == 1:
        add_Expense()
    
    elif option == 2:
        view_Expenses()
    
    elif option == 3:
        total_Expense()
    
    elif option == 4:
        category_Summary()
    
    elif option == 5:
        delete_Expense()
    
    elif option == 6:
        filter_By_Category()
    
    elif option == 7:
        break

    else:
        print("Invalid Option !!")