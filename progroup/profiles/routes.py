from flask import (
    Flask, flash, render_template, redirect, request, session, url_for, Blueprint)
from bson.objectid import ObjectId
from progroup import mongo

# Create a profiles object as a blueprint
profiles = Blueprint('profiles', __name__)


@profiles.route("/get_profiles")
def get_profiles():
    profiles = list(mongo.db.profiles.find())
    return render_template("profiles/profiles.html", profiles=profiles)


@profiles.route("/add_profile", methods=["GET", "POST"])
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
        return redirect(url_for("profiles/profiles"))

    profiles = mongo.db.profiles.find()
    return render_template("profiles/add_profile.html", profiles=profiles)


@profiles.route("/edit_profile/<profile_id>", methods=["GET", "POST"])
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
        return redirect(url_for("profiles/profiles"))

    profile = mongo.db.profiles.find_one({"_id": ObjectId(profile_id)})
    return render_template("profiles/edit_profile.html", profile=profile)


@profiles.route('/delete_profile/<profile_id>')
def delete_profile(profile_id):
    mongo.db.profiles.delete_one({"_id": ObjectId(profile_id)})
    flash("Profile Deleted")
    return redirect(url_for("profiles/profiles"))