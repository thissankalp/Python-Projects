from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def greet():
    if request.method == "POST":
        username = request.form["username"]
        return f"Hello, {username}"
    return render_template("greeting_user.html")

if __name__ == "__main__":
    app.run(debug = True)