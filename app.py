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
    profiles = list(mongo.db.profiles.find())
    return render_template("profiles.html", profiles=profiles)


@app.route("/add_profile", methods=["GET", "POST"])
def add_profile():
    if request.method == "POST": 
        profiles = {
            "group_name": request.form.get('group_name'),
            "contact_name": request.form.get('contact_name'), 
            "contact_email": request.form.get('contact_email'), 
            "contact_phone": request.form.get('contact_phone'), 
            "line_address": request.form.get('line_address'), 
            "city": request.form.get('city'),
            "postcode": request.form.get('postcode'),
            "country": request.form.get('country'),
        }

        mongo.db.profiles.insert_one(profiles)
        flash("User Successfully Added")
        return redirect(url_for("profiles"))

    profiles = mongo.db.profiles.find()
    return render_template("add_profile.html", profiles=profiles)


@app.route('/delete_profile/<profile_id>')
def delete_profile(profile_id):
    mongo.db.profiles.delete_one({"_id": ObjectId(profile_id)})
    return redirect(url_for("profiles"))


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
            "password": request.form.get('city'),
            "position": request.form.get('position'),
            "is_admin": is_admin 
        }

        mongo.db.users.insert_one(users)
        return redirect(url_for("users"))

    users = mongo.db.users.find()
    return render_template("add_user.html", users=users)


@app.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if request.method == "POST":
        is_admin = "admin" if request.form.get("is_admin") else "user" 
        updated_user = {"$set": 
        {
             "username": request.form.get('username'),
            "first_name": request.form.get('first_name'), 
            "last_name": request.form.get('last_name'), 
            "email": request.form.get('email'), 
            "password": request.form.get('city'),
            "position": request.form.get('position'),
            "is_admin": is_admin 
        }
        }

        mongo.db.users.update_one({"_id": ObjectId(user_id)}, updated_user)
        return redirect(url_for("users"))

    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("edit_user.html", user=user)


@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    return redirect(url_for("users"))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)