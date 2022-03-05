from flask import (
    flash, render_template, redirect, request, session, url_for, Blueprint)
from bson.objectid import ObjectId
from werkzeug.security import check_password_hash
from progroup import mongo


# Create an authentication object as a blueprint
authentication = Blueprint('authentication', __name__)


@authentication.route("/")
@authentication.route("/login", methods=["GET", "POST"])
def login() -> object:
    """
    Render login.html when user navigate to the webaddress.
    Page will display the login form with username and
    password and login button. System will check whether user exist
    and if the password entered matching the database data it will
    put the username in session and login the user.
    :return render_template of get_reservation.html
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
             existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for('reservations.get_reservations'))

            else:
                # invalid password match
                flash("Incorrect Password")
                return redirect(url_for("authentication.login"))

        else:
            # username doesn't exist
            flash("Incorrect Username")
            return redirect(url_for("authentication.login"))

    return render_template("authentication/login.html")


@authentication.route("/authentication.logout")
def logout() -> object:
    """
    Render login.html page and popping user from session.
    :retrun render_template of login.html
    """
    # remove user from session cookie
    session.pop("user")
    return redirect(url_for("authentication.login"))


@authentication.route("/account", methods=["GET"])
def account():
    """
    This function renders the profile page and displays
    the users profile information once the user is logged in
    and exists in the users collection
    :param username: username of user
    :return render_template of account.html
    """
    # If the user is not logged in, redirect them to home/landing page
    if 'user' not in session:
        return redirect(url_for("authentication.login"))

    total = "Number of Groups: " + str(mongo.db.reservations.
                                       count_documents({}))
    stat1 = "Confirmed Groups: " + str(mongo.db.reservations.count_documents(
        {"status": "confirmed"}))
    stat2 = "Provisional Groups: " + str(mongo.db.reservations.count_documents(
        {"status": "provisional"}))
    stat3 = "Cancelled Groups: " + str(mongo.db.reservations.count_documents(
        {"status": "cancelled"}))

    # Find the user in the users collection
    username = session['user']
    user = mongo.db.users.find_one({"username": username})
    return render_template("users/account.html",
                           user=user,
                           total=total,
                           stat1=stat1,
                           stat2=stat2,
                           stat3=stat3)


@authentication.route("/edit_account/<user_id>", methods=["GET", "POST"])
def edit_account(user_id):
    """
    Render edit_account.html page after the user clicked on the edit button
    once all changes are entered in the input fields the selected documents
    values will be updated by clicking on the Save Changes button or Abort the
    process with the Cancel button and return to gaccount.html page
    :return render_template of account.html page
    """

    # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))

    if request.method == "POST":
        is_admin = "admin" if request.form.get("is_admin") else "user"
        updated_user = {"$set": {
            "first_name": request.form.get('first_name'),
            "last_name": request.form.get('last_name'),
            "email": request.form.get('email'),
            "position": request.form.get('position'),
            "is_admin": is_admin
        }
        }

        mongo.db.users.update_one({"_id": ObjectId(user_id)}, updated_user)
        flash("Account Updated")
        return redirect(url_for("authentication.account"))

    total = "Total Users: " + str(mongo.db.users.count_documents({}))
    stat1 = "Admins: " + str(mongo.db.users.count_documents(
        {"is_admin": "admin"}))
    stat2 = "Users: " + str(mongo.db.users.count_documents(
        {"is_admin": "user"}))
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("users/edit_account.html",
                           total=total,
                           stat1=stat1,
                           stat2=stat2,
                           user=user)
