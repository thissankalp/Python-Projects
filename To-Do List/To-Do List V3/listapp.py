from flask import Flask,render_template, request, redirect, url_for
import json
tasks = [] 

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []

def save_task():
    with open("tasks.json", "w")as f:
        json.dump(tasks, f, indent=4)

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def listhome():
    if request.method == "POST":
        task = request.form["task"].strip()
        if not task:
            return redirect(url_for("listhome"))
        tasks.append(task)
        print(tasks)
        save_task()
    return render_template("listindex.html", tasks = tasks)

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_task()
    return redirect(url_for("listhome"))

load_tasks()
if __name__ == "__main__":
    app.run(debug=True)