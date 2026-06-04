from flask import Flask, redirect, render_template, request, url_for
import json

expenses = []
def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []

def save_expense():
    with open("expenses.json", "w")as f:
        json.dump(expenses, f, indent=4)

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def homepage():
    if request.method == "POST":
        category = request.form["category"]
        try:
            amount = float(request.form["amount"])
        except ValueError:
            return "Invalid Amount"
        description = request.form["description"]

        expense ={
            "category" : category,
            "amount" : amount,
            "description" : description
        }
        expenses.append(expense)
        save_expense()
        print(expenses)
        return redirect(url_for("homepage"))
    
    total = 0
    for expense in expenses:
        total += expense["amount"]
    
    summary = {}
    for expense in expenses:
        category = expense["category"]
        if category not in summary:
            summary[category] = 0
        summary[category] += expense["amount"]
    return render_template("Exp.html", expenses = expenses, total = total, summary = summary)

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_expense()
    return redirect(url_for("homepage"))

load_expenses()
if __name__ == "__main__":
    app.run(debug=True)