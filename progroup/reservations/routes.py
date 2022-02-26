from datetime import datetime
from flask import (
    flash, render_template, redirect, session, request, url_for, Blueprint)
from bson.objectid import ObjectId
from flask_paginate import Pagination
from progroup import mongo
from progroup.util import util

# Create a users object as a blueprint
reservations = Blueprint('reservations', __name__)


@reservations.route("/get_reservations")
def get_reservations() -> object:
    """
    render the get_reservations.html template once the user has a succesful
    login and dispaly all the reservations available in the reservations
    collection and sort it by group name
    :return render_template of get_reservations.html
    """
    # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))
    offset, per_page, page = util.setup_pagination()

    total = "Number of Groups: " + str(mongo.db.reservations.count_documents({}))
    stat1 = "Confirmed Groups: " + str(mongo.db.reservations.count_documents({"status": "confirmed"}))
    stat2 = "Provisional Groups: " + str(mongo.db.reservations.count_documents({"status": "provisional"}))
    stat3 = "Cancelled Groups: " + str(mongo.db.reservations.count_documents({"status": "cancelled"}))
    total_reservations = mongo.db.reservations.count_documents({})
    reservations = mongo.db.reservations.find().sort("group_name", 1)
    reservations_paginated = reservations[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total_reservations, css_framework='bootstrap')
    return render_template("reservations/reservations.html",
                            reservations=reservations_paginated,
                            page=page,
                            per_page=per_page,
                            pagination=pagination,
                            total=total,
                            stat1=stat1,
                            stat2=stat2,
                            stat3=stat3)


@reservations.route("/add_reservation", methods=["GET", "POST"])
def add_reservation() -> object:
    """
    render add_reservation html page after teh user clicked on the
    Add New Reservation button and add to the database
    the new reservation once all input fields are filled
    :return render_template of get_reservations.html
    """

    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d, %H:%M:%S")

    # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))

    if request.method == "POST":
        try:
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
                "porterage": request.form.get('porterage'),
                "single_room": request.form.get('single_room'),
                "double_room": request.form.get('double_room'),
                "twin_room": request.form.get('twin_room'),
                "triple_room": request.form.get('triple_room'),
                "rooms": request.form.get('rooms'),
                "single_rate": request.form.get('single_rate'),
                "double_rate": request.form.get('double_rate'),
                "twin_rate": request.form.get('twin_rate'),
                "triple_rate": request.form.get('triple_rate'),
                "pax": request.form.get('pax'),
                "notes": request.form.get('notes'),
                "created_by": session["user"],
                "created_on": timestamp,
            }

            mongo.db.reservations.insert_one(reservations)
            flash("Reservation Added")
        except Exception as e:
            flash("An exception occurred when adding the reservation: " +
                  getattr(e, 'message', repr(e)))
            return redirect(url_for("reservations.get_reservations"))

    total = "Number of Groups: " + str(mongo.db.reservations.count_documents({}))
    stat1 = "Confirmed Groups: " + str(mongo.db.reservations.count_documents({"status": "confirmed"}))
    stat2 = "Provisional Groups: " + str(mongo.db.reservations.count_documents({"status": "provisional"}))
    stat3 = "Cancelled Groups: " + str(mongo.db.reservations.count_documents({"status": "cancelled"}))
    profiles = mongo.db.profiles.find().sort("group_name", 1)
    return render_template("reservations/add_reservation.html",
                            profiles=profiles,
                            total=total,
                            stat1=stat1,
                            stat2=stat2,
                            stat3=stat3)


@reservations.route("/search", methods=["GET", "POST"])
def search() -> object:
    """
    search function for reservation what can search/filter for group name
    and status
    """
    offset, per_page, page = util.setup_pagination()
    query = request.form.get("query")
    total_reservations = mongo.db.reservations.count_documents({"$text":
                                                    {"$search": query}})
    reservations = list(mongo.db.reservations.find({"$text":
                                                    {"$search": query}}))
    reservations_paginated = reservations[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total_reservations, css_framework='bootstrap')
    total = "Number of Groups: " + str(mongo.db.reservations.count_documents({}))
    stat1 = "Confirmed Groups: " + str(mongo.db.reservations.count_documents({"status": "confirmed"}))
    stat2 = "Provisional Groups: " + str(mongo.db.reservations.count_documents({"status": "provisional"}))
    stat3 = "Cancelled Groups: " + str(mongo.db.reservations.count_documents({"status": "cancelled"}))
    
    flash("Search filter applied '" + query.upper() + "'")
    return render_template("reservations/reservations.html",                       
                            reservations=reservations_paginated,
                            page=page,
                            per_page=per_page,
                            pagination=pagination,
                            total=total,
                            stat1=stat1,
                            stat2=stat2,
                            stat3=stat3)


@reservations.route('/edit_reservation<reservation_id>', methods=["GET", "POST"])
def edit_reservation(reservation_id) -> object:
    """
    render edit_reservation.html page with the reservation values as per the id
    after the user clicked on the edit button
    once all changes are entered in the input fields the database collect
    value will be updated accordingly by clicking on the Save Changes button or
    Abort the process with the Cancel button and return to
    get_reservation.html page
    :return render_template of get_reservations.html page
    """

    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d, %H:%M:%S")

    # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))

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
            "porterage": request.form.get('porterage'),
            "single_room": request.form.get('single_room'),
            "double_room": request.form.get('double_room'),
            "twin_room": request.form.get('twin_room'),
            "triple_room": request.form.get('triple_room'),
            "rooms": request.form.get('rooms'),
            "single_rate": request.form.get('single_rate'),
            "double_rate": request.form.get('double_rate'),
            "twin_rate": request.form.get('twin_rate'),
            "triple_rate": request.form.get('triple_rate'),
            "pax": request.form.get('pax'),
            "notes": request.form.get('notes'),
            "last_updated_by": session["user"],
            "last_updated_on": timestamp,
        }
        }
        mongo.db.reservations.update_one({"_id": ObjectId(reservation_id)},
                                            updated_reservation)
        flash("Reservation Updated")
        return redirect(url_for("reservations.get_reservations"))

    total = "Number of Groups: " + str(mongo.db.reservations.count_documents({}))
    stat1 = "Confirmed Groups: " + str(mongo.db.reservations.count_documents({"status": "confirmed"}))
    stat2 = "Provisional Groups: " + str(mongo.db.reservations.count_documents({"status": "provisional"}))
    stat3 = "Cancelled Groups: " + str(mongo.db.reservations.count_documents({"status": "cancelled"}))
    profiles = mongo.db.profiles.find().sort("category_name", 1)
    reservation = mongo.db.reservations.find_one({"_id": ObjectId(reservation_id)})
    return render_template("reservations/edit_reservation.html",
                            reservation=reservation,
                            profiles=profiles,
                            total=total,
                            stat1=stat1,
                            stat2=stat2,
                            stat3=stat3)


@reservations.route('/delete_reservation/<reservation_id>')
def delete_reservation(reservation_id) -> object:
    """
    delete the selected document as per user id from the reservations
    collection and returns to list of remaining reservations
    :return render_template of get_reservation.html
    """
    # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))

    mongo.db.reservations.delete_one({"_id": ObjectId(reservation_id)})
    flash("Reservation Deleted")
    return redirect(url_for("reservations.get_reservations"))


@reservations.route("/contact", methods=["GET", "POST"])
def contact() -> object:
    """
    Render the contact.html template where the user can send email to the site
    owner the email function is powered with email.js see static/js/email.js
    :return render_template of contact.html
    """

    # Check the user is logged in
    if 'user' not in session:
        return redirect(url_for("authentication.login"))

    total = "Number of Groups: " + str(mongo.db.reservations.count_documents({}))
    stat1 = "Confirmed Groups: " + str(mongo.db.reservations.count_documents({"status": "confirmed"}))
    stat2 = "Provisional Groups: " + str(mongo.db.reservations.count_documents({"status": "provisional"}))
    stat3 = "Cancelled Groups: " + str(mongo.db.reservations.count_documents({"status": "cancelled"}))
    return render_template("email/contact.html",
                            total=total,
                            stat1=stat1,
                            stat2=stat2,
                            stat3=stat3)
