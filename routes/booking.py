from flask import Blueprint, request, jsonify
from models.booking import booking_collection

bp = Blueprint("booking", __name__)

@bp.route("/create_booking", methods=["POST"])
def create_booking():
    #required keys/variables for every POST request
    # booking_id, driver_id, commuter_id, pickup_location, dropoff_location, fare, status
    data = request.get_json()
    booking_collection.insert_one(data)
    return jsonify({"message": "Booking created successfully!"})

@bp.route("/cancel_booking", methods=["POST"]) # You can use Update function to change the status of the booking
def cancel_booking():
    data = request.get_json()
    booking_collection.update_one(
        {"booking_id": data["booking_id"]},
        {"$set": {"status": "cancelled", "cancellation_reason": data["cancellation_reason"]}} # accept string from frontend for status
    )
    return jsonify({"message": "Booking cancelled!"})