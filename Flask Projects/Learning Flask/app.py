from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    name = "Sankalp"
    return render_template("about.html", name = name)

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name = name)

if __name__ == "__main__":
    app.run(debug = True)
