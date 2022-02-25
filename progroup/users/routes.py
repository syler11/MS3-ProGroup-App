from flask import (
    flash, render_template, redirect, request, session, url_for, Blueprint)
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash
from progroup import mongo

# Create a users object as a blueprint
users = Blueprint('users', __name__)


@users.route("/get_users")
def get_users():
    """
    Render get_users.html page after user click on the Users button
    in the navigation.
    Displays all current users and their details a gives and an option
    to create new user or edit and delete exisitng user.
    Only visible to users with admin role.
    :return render_template of get_users.html
    """

    # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))
    
    total = "Total Users: " + str(mongo.db.users.count_documents({}))
    stat1 = "Admins: " + str(mongo.db.users.count_documents({"is_admin": "admin"}))
    stat2 = "Users: " + str(mongo.db.users.count_documents({"is_admin": "user"}))

    users_list = list(mongo.db.users.find())
    return render_template("users/users.html", 
                            total=total,
                            stat1=stat1,
                            stat2=stat2,
                            users_list=users_list)


@users.route("/add_user", methods=["GET", "POST"])
def add_user():
    """
    Render add_user.html page after the user selected the
    Add New button.
    The new document will be added to the users collection
    once all input fields are filled
    :return render_template of add_user.html
    """

    # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))

    if request.method == "POST":
        is_admin = "admin" if request.form.get("is_admin") else "user"
        add_users = {
            "username": request.form.get('username'),
            "first_name": request.form.get('first_name'),
            "last_name": request.form.get('last_name'),
            "email": request.form.get('email'),
            "password": generate_password_hash(request.form.get('password')),
            "position": request.form.get('position'),
            "is_admin": is_admin
        }

        mongo.db.users.insert_one(add_users)
        flash("User Added")
        return redirect(url_for("users.get_users"))

    total = "Total Users: " + str(mongo.db.users.count_documents({}))
    stat1 = "Admins: " + str(mongo.db.users.count_documents({"is_admin": "admin"}))
    stat2 = "Users: " + str(mongo.db.users.count_documents({"is_admin": "user"}))
    users_list = mongo.db.users.find()
    return render_template("users/add_user.html", 
                            total=total,
                            stat1=stat1,
                            stat2=stat2,
                            users_list=users_list)


@users.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    """
    Render edit_reservation.html page after the user clicked on the edit button
    once all changes are entered in the input fields the selected documents
    values will be updated by clicking on the Save Changes button or Abort the
    process with the Cancel button and return to get_users.html page
    :return render_template of get_users.html page
    """

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

    total = "Total Users: " + str(mongo.db.users.count_documents({}))
    stat1 = "Admins: " + str(mongo.db.users.count_documents({"is_admin": "admin"}))
    stat2 = "Users: " + str(mongo.db.users.count_documents({"is_admin": "user"}))
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("users/edit_user.html", 
                            total=total,
                            stat1=stat1,
                            stat2=stat2,
                            user=user)


@users.route('/delete_user/<user_id>')
def delete_user(user_id):
    """
    delete the selected document from the users collection and returns to
    list of remaining reservations
    :return render_template of get_users.html
    """
    # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))

    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    flash("User Deleted")
    return redirect(url_for("users.get_users"))
