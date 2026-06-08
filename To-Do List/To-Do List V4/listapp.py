from flask import Flask,render_template, request, redirect, url_for
import sqlite3

def get_db():
    return sqlite3.connect("tasks.db")

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def listhome():
    conn = get_db()
    cursor = conn.cursor()

    if request.method == "POST":
        task = request.form["task"].strip()
        if task:
            cursor.execute("INSERT INTO tasks(task) VALUES(?)", (task,))
            conn.commit()
            conn.close()
            return redirect(url_for("listhome"))
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return render_template("listindex.html", tasks = tasks)

@app.route("/delete/<int:index>")
def delete(index):
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM tasks WHERE id=?", (index, ))
    conn.commit()
    conn.close()
    return redirect(url_for("listhome"))

@app.route("/edit/<int:index>", methods = ["GET", "POST"])
def edit(index):
    conn = get_db()
    cursor = conn.cursor()

    if request.method == "POST":
        new_task = request.form["task"].strip()
        cursor.execute("UPDATE tasks SET task=? WHERE id=?",(new_task, index, ))
        conn.commit()
        conn.close()
        return redirect(url_for("listhome"))
    cursor.execute("SELECT * FROM tasks WHERE id=?", (index,))
    task = cursor.fetchone()
    if task is None:
        conn.close()
        return redirect(url_for("listhome"))
    conn.close()
    return render_template("edit.html", task = task)

if __name__ == "__main__":
    app.run(debug=True)