from flask import (
    Flask, flash, render_template, redirect, request, session, url_for, Blueprint)
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from progroup import mongo

# Create a users object as a blueprint
users = Blueprint('users', __name__)


@users.route("/get_users")
def get_users():

      # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))

    users = list(mongo.db.users.find())
    return render_template("users/users.html", users=users)


@users.route("/add_user", methods=["GET", "POST"])
def add_user():

  # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))

    if request.method == "POST":
        is_admin = "admin" if request.form.get("is_admin") else "user" 
        users = {
            "username": request.form.get('username'),
            "first_name": request.form.get('first_name'), 
            "last_name": request.form.get('last_name'), 
            "email": request.form.get('email'), 
            "password": generate_password_hash(request.form.get('password')),
            "position": request.form.get('position'),
            "is_admin": is_admin 
        }

        mongo.db.users.insert_one(users)
        flash("User Added")
        return redirect(url_for("users.get_users"))

    users = mongo.db.users.find()
    return render_template("users/add_user.html", users=users)


@users.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):

  # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))

    if request.method == "POST":
        is_admin = "admin" if request.form.get("is_admin") else "user" 
        updated_user = {"$set": 
        {
             "username": request.form.get('username'),
            "first_name": request.form.get('first_name'), 
            "last_name": request.form.get('last_name'), 
            "email": request.form.get('email'), 
            "position": request.form.get('position'),
            "is_admin": is_admin 
        }
        }

        mongo.db.users.update_one({"_id": ObjectId(user_id)}, updated_user)
        flash("User Updated")
        return redirect(url_for("users.get_users"))

    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("users/edit_user.html", user=user)


@users.route('/delete_user/<user_id>')
def delete_user(user_id):

  # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))

    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    flash("User Deleted")
    return redirect(url_for("users.get_users"))