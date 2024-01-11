from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html", name="World")


@app.get("/ping")
def ping():
    print("Ping")
    return """<button hx-get="/pong" hx-swap="outerHTML">Pong</button>"""


@app.get("/pong")
def pong():
    print("Pong")
    return """<button hx-get="/ping" hx-swap="outerHTML">Ping</button>"""


if __name__ == "__main__":
    app.run(debug=True)
