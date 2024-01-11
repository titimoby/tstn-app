from flask import Flask, render_template, request
from typing import List
from enum import Enum
import duckdb


class Status(Enum):
    REGISTERED = "REGISTERED"
    UNKNOWN = "UNKNOWN"


class RegisteredClient:
    def __init__(self, ip: str, status: Status):
        self.ip = ip
        self.status = status


# route flask for index.html
app = Flask(__name__)
db = duckdb.connect(database=":memory:", read_only=False)
db.execute(
    "CREATE TABLE clients (  \
           ip VARCHAR,       \
           status VARCHAR,   \
           UNIQUE(ip)        \
           )"
)


def db_insert_client(ip: str):
    query = f"INSERT OR REPLACE INTO clients (ip, status) VALUES ('{ip}', '{Status.REGISTERED.value}')"
    db.execute(query)


def db_get_clients():
    query = "SELECT ip, status FROM clients"
    result = db.execute(query).fetchall()
    clients = []
    for row in result:
        ip, status = row
        clients.append(RegisteredClient(ip, Status(status)))
    return clients


@app.route("/")
def index():
    return render_template("index.html", registered_clients=db_get_clients())


@app.route("/register")
def register():
    ip = request.remote_addr
    db_insert_client(ip)
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=3000)
