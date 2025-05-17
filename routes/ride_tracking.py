from flask import Blueprint, request, jsonify
from flask_socketio import emit
from models.ride_tracking import ride_tracking_collection
from main import socketio

bp = Blueprint("ride_tracking", __name__)

@bp.route("/update_location", methods=["POST"])
def update_location():
    data = request.get_json()
    ride_tracking_collection.update_one(
        {"booking_booking_id": data["booking_booking_id"]},
        {"$set": {"latitude": data["latitude"], "longitude": data["longitude"]}},
        upsert=True
    )
    socketio.emit("location_update", data)
    return jsonify({"message": "Location updated!"})

@socketio.on("request_location")
def send_location(data):
    ride_data = ride_tracking_collection.find_one({"booking_booking_id": data["booking_booking_id"]})
    emit("location_update", ride_data)