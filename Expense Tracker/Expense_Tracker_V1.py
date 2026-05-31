expenses = []

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
    print("Expense Added")

def view_Expenses():
    if(len(expenses) == 0):
        print("No expenses Available !!")
        return
    
    print("===== All Expenses =====")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Category : {expense['category']} - Amount : ₹{expense['amount']:.2f} - Description : {expense['description']}")


def total_Expense():
    total = 0

    for expense in expenses:
        total += expense['amount']
    print(f"Total Expense : ₹{total:.2f}")

while True :
    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

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
        break

    else:
        print("Invalid Option !!")