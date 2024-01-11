from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html", name="World")


@app.get("/register")
def register():
    response = requests.get("http://127.0.0.1:3000/register")
    print(response.text)
    return """<h2>Register done</h2>"""


if __name__ == "__main__":
    app.run(debug=True)
