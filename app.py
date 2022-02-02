import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for, Blueprint)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import requests
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for('reservations'))

            else:
                # invalid password match
                flash("Incorrect Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username")
            return redirect(url_for("login"))

    return render_template("authentication/login.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/reservations")
def reservations():
    find = {}
    total_groups = mongo.db.reservations.count_documents(find)
    reservations = mongo.db.reservations.find().sort("group_name", 1)
    return render_template("reservations/reservations.html", reservations=reservations, total_groups=total_groups)


@app.route("/add_reservation", methods=["GET", "POST"])
def add_reservation():
    if request.method == "POST": 
        reservations = {
            "group_name": request.form.get('group_name'),
            "arrival_date": request.form.get('arrival_date'), 
            "contact_name": request.form.get('contact_name'), 
            "contact_email": request.form.get('contact_email'), 
            "contact_phone": request.form.get('contact_phone'), 
            "line_address": request.form.get('line_address'), 
            "city": request.form.get('city'),
            "postcode": request.form.get('postcode'),
            "country": request.form.get('country'),
            "los": request.form.get('los'), 
            "status": request.form.get('status'), 
            "board": request.form.get('board'), 
            "single_room": request.form.get('single_room'),
            "double_room": request.form.get('double_room'),
            "twin_room": request.form.get('twin_room'),
            "triple_room": request.form.get('triple_room'),
            "single_rate": request.form.get('single_rate'),
            "double_rate": request.form.get('double_rate'),
            "twin_rate": request.form.get('twin_rate'),
            "triple_rate": request.form.get('triple_rate'),
            "notes": request.form.get('notes'),
        }

        mongo.db.reservations.insert_one(reservations)
        flash("Reservation Added")
        return redirect(url_for("reservations"))
    
    profiles = mongo.db.profiles.find().sort("group_name", 1)
    return render_template("reservations/add_reservation.html", profiles=profiles)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    reservations = list(mongo.db.reservations.find({"$text": {"$search": query}}))
    flash("Search filter applied")
    return render_template("reservations/reservations.html", reservations=reservations)


@app.route('/edit_reservation<reservation_id>', methods=["GET", "POST"])
def edit_reservation(reservation_id):
    if request.method == "POST":
        updated_reservation = {"$set": 
        {
            "group_name": request.form.get('group_name'),
            "arrival_date": request.form.get('arrival_date'), 
            "contact_name": request.form.get('contact_name'), 
            "contact_email": request.form.get('contact_email'), 
            "contact_phone": request.form.get('contact_phone'), 
            "line_address": request.form.get('line_address'), 
            "city": request.form.get('city'),
            "postcode": request.form.get('postcode'),
            "country": request.form.get('country'),
            "los": request.form.get('los'), 
            "status": request.form.get('status'), 
            "board": request.form.get('board'), 
            "single_room": request.form.get('single_room'),
            "double_room": request.form.get('double_room'),
            "twin_room": request.form.get('twin_room'),
            "triple_room": request.form.get('triple_room'),
            "single_rate": request.form.get('single_rate'),
            "double_rate": request.form.get('double_rate'),
            "twin_rate": request.form.get('twin_rate'),
            "triple_rate": request.form.get('triple_rate'),
            "notes": request.form.get('notes'),
        }
        }
        mongo.db.reservations.update_one({"_id": ObjectId(reservation_id)}, updated_reservation)
        flash("Reservation Updated")
        return redirect(url_for("reservations"))
    
    profiles = mongo.db.profiles.find().sort("category_name", 1)
    reservation = mongo.db.reservations.find_one({"_id": ObjectId(reservation_id)})
    return render_template("reservations/edit_reservation.html", reservation=reservation, profiles=profiles)


@app.route('/delete_reservation/<reservation_id>')
def delete_reservation(reservation_id):
    mongo.db.reservations.delete_one({"_id": ObjectId(reservation_id)})
    flash("Reservation Deleted")
    return redirect(url_for("reservations"))


@app.route("/profiles")
def profiles():
    profiles = list(mongo.db.profiles.find())
    return render_template("profiles/profiles.html", profiles=profiles)


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
        flash("Profile Added")
        return redirect(url_for("profiles"))

    profiles = mongo.db.profiles.find()
    return render_template("profiles/add_profile.html", profiles=profiles)


@app.route("/edit_profile/<profile_id>", methods=["GET", "POST"])
def edit_profile(profile_id):
    if request.method == "POST":
        updated_profile = {"$set": 
        {
             "group_name": request.form.get('group_name'),
            "contact_name": request.form.get('contact_name'), 
            "contact_email": request.form.get('contact_email'), 
            "contact_phone": request.form.get('contact_phone'), 
            "line_address": request.form.get('line_address'), 
            "city": request.form.get('city'),
            "postcode": request.form.get('postcode'),
            "country": request.form.get('country'),
        }
        }
        mongo.db.profiles.update_one({"_id": ObjectId(profile_id)}, updated_profile)
        flash("Profile Updated")
        return redirect(url_for("profiles"))

    profile = mongo.db.profiles.find_one({"_id": ObjectId(profile_id)})
    return render_template("profiles/edit_profile.html", profile=profile)


@app.route('/delete_profile/<profile_id>')
def delete_profile(profile_id):
    mongo.db.profiles.delete_one({"_id": ObjectId(profile_id)})
    flash("Profile Deleted")
    return redirect(url_for("profiles"))


@app.route("/users")
def users():
    users = list(mongo.db.users.find())
    return render_template("users/users.html", users=users)


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
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
        return redirect(url_for("users"))

    users = mongo.db.users.find()
    return render_template("users/add_user.html", users=users)


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
            "position": request.form.get('position'),
            "is_admin": is_admin 
        }
        }

        mongo.db.users.update_one({"_id": ObjectId(user_id)}, updated_user)
        flash("User Updated")
        return redirect(url_for("users"))

    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("users/edit_user.html", user=user)


@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    flash("User Deleted")
    return redirect(url_for("users"))


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("email/contact.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)