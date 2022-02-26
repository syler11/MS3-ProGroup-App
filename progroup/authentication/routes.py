from flask import (
    flash, render_template, redirect, request, session, url_for, Blueprint)
from werkzeug.security import check_password_hash
from progroup import mongo


# Create an authentication object as a blueprint
authentication = Blueprint('authentication', __name__)


@authentication.route("/")
@authentication.route("/login", methods=["GET", "POST"])
def login() -> object:
    """
    Render login.html when user navigate to the webadress.
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
    # Find the user in the users collection
    username = session['user']
    user = mongo.db.users.find_one({"username": username})
    return render_template("users/account.html",
                            user=user)