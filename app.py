import os
from flask import (
    Flask, flash, render_template, url_for)
from flask_pymongo import pymongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def reservations():
    return render_template("reservations.html")


@app.route("/profiles")
def profiles():
    return render_template("profiles.html")


@app.route("/users")
def users():
    return render_template("users.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)