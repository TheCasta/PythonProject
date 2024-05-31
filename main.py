import sqlite3
from flask import Flask, request, g, jsonify, send_file
import json

app = Flask(__name__, static_url_path='', static_folder='static')

DATABASE = r'/home/casta/Scrivania/Progetto/data/database.sqlite'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def get_cursor():
    return get_db().cursor()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def main():
    return send_file('static/index.html')

@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "GET":
        tasks = get_cursor().execute("SELECT * FROM tasks;").fetchall()
        return json.dumps(tasks)
    elif request.method == "POST":
        data = request.json
        title = data.get("title")
        description = data.get("description")
        due_date = data.get("due_date")
        cursor = get_cursor()
        cursor.execute("INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)", (title, description, due_date))
        get_db().commit()
        return jsonify({"status": "success"}), 201

if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
