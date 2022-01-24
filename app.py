import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
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


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        is_admin = "admin" if request.form.get("is_admin") else "user" 
        users = {
            "username": request.form.get('username'),
            "first_name": request.form.get('first_name'), 
            "last_name": request.form.get('last_name'), 
            "email": request.form.get('email'), 
            "position": request.form.get('position'), 
            "password": request.form.get('password'),
            "is_admin": is_admin 
        }

        mongo.db.users.insert_one(users)
        flash("User Successfully Added")
        return redirect(url_for("users"))

    users = mongo.db.users.find()
    return render_template("add_user.html", users=users)


@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    return redirect(url_for("users"))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)