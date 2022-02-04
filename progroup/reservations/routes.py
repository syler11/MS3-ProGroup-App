from flask import (
    Flask, flash, render_template, redirect, request, url_for, Blueprint)
from bson.objectid import ObjectId
from progroup import mongo

# Create a users object as a blueprint
reservations = Blueprint('reservations', __name__)


@reservations.route("/get_reservations")
def get_reservations():
    """
    Render the get_reservations.html template once the user has a succesful login 
    and dispaly all the reservations available in the reservations collection 
    and sort it by group name
    :return render_template of get_reservations.html
    """
    total_groups = mongo.db.reservations.count_documents({})
    reservations = mongo.db.reservations.find().sort("group_name", 1)
    return render_template("reservations/reservations.html", reservations=reservations, total_groups=total_groups)


@reservations.route("/add_reservation", methods=["GET", "POST"])
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


@reservations.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    reservations = list(mongo.db.reservations.find({"$text": {"$search": query}}))
    flash("Search filter applied")
    return render_template("reservations/reservations.html", reservations=reservations)


@reservations.route('/edit_reservation<reservation_id>', methods=["GET", "POST"])
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


@reservations.route('/delete_reservation/<reservation_id>')
def delete_reservation(reservation_id):
    mongo.db.reservations.delete_one({"_id": ObjectId(reservation_id)})
    flash("Reservation Deleted")
    return redirect(url_for("reservations"))


@reservations.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("email/contact.html")