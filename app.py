import os
from flask import (
    Flask, flash, render_template, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def reservations():
    return render_template("reservations.html")


@app.route("/profiles")
def profiles():
    return render_template("profiles.html")


@app.route("/users")
def users():
    users = list(mongo.db.users.find())
    return render_template("users.html", users=users)


@app.route("/add_user")
def add_user():
    return render_template("add_user.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)