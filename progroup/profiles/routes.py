from flask import (
    flash, render_template, redirect, request, session, url_for, Blueprint)
from bson.objectid import ObjectId
from progroup import mongo

# Create a profiles object as a blueprint
profiles = Blueprint('profiles', __name__)


@profiles.route("/get_profiles")
def get_profiles() -> object:
    """
    Render get_profiles html page and user clicked on the profiles
    navigation button. It will list all the existing Profiles in the system
    with and edit and delete and Add New button.
    :return render_template of get_profiles.html
    """

    # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))

    profiles_list = list(mongo.db.profiles.find())
    return render_template("profiles/profiles.html", profiles_list=profiles_list)


@profiles.route("/add_profile", methods=["GET", "POST"])
def add_profile() -> object:
    """
    Render add_profiles html page
    :return render_template of get_profiles.html
    """

    # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))

    if request.method == "POST":
        add_profiles = {
            "group_name": request.form.get('group_name'),
            "contact_name": request.form.get('contact_name'),
            "contact_email": request.form.get('contact_email'),
            "contact_phone": request.form.get('contact_phone'),
            "line_address": request.form.get('line_address'),
            "city": request.form.get('city'),
            "postcode": request.form.get('postcode'),
            "country": request.form.get('country'),
        }

        mongo.db.profiles.insert_one(add_profiles)
        flash("Profile Added")
        return redirect(url_for("profiles.get_profiles"))

    profiles_list = mongo.db.profiles.find()
    return render_template("profiles/add_profile.html", profiles_list=profiles_list)


@profiles.route("/edit_profile/<profile_id>", methods=["GET", "POST"])
def edit_profile(profile_id) -> object:
    """
    Render edit_profile html page after the user clicked on the edit button
    once all changes are entered in the input fields the selected documents
    values will be updated by clicking on the Save Changes button or Abort the
    process with the Cancel button and return to get_profiles.html page
    :return render_template of get_profiles.html page
    """

    # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))

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
def delete_profile(profile_id) -> object:
    """
    delete the selected document from the profiles collection and returns to
    list of remaining profiles
    :return render_template of get_users.html
    """

    # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))

    mongo.db.profiles.delete_one({"_id": ObjectId(profile_id)})
    flash("Profile Deleted")
    return redirect(url_for("profiles.get_profiles"))
