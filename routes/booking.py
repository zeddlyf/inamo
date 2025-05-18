from flask import Blueprint, request, jsonify, Response
from models.booking import booking_collection
from utils.dijkstra import Dijkstra
import datetime
from bson import ObjectId,json_util

bp = Blueprint("booking", __name__)

@bp.route("/create_booking", methods=["POST"])
def create_booking():
    #required keys/variables for every POST request
    # booking_id, driver_id, commuter_id, pickup_location, dropoff_location, fare, status
    
    data = request.get_json()
    
    required_keys = ["commuter_commuter_id", "driver_driver_id",
                    "pickup_location",
                    "drop_off_location",
                    "status", "promo_code",
                    ]
    for key in required_keys:
        if key not in data:
            return jsonify({"error": f"Missing required field: {key}"}), 400
        
    d = Dijkstra()
    distance, estimated_eta = Dijkstra.dijkstra(d.graph, data["pickup_location"], data["drop_off_location"])
    # print(shortest_path)
    estimated_fare = Dijkstra.calculate_fare(distance)

    booking = {
        # "commuter_commuter_id": data["commuter_commuter_id"],
        # "driver_driver_id": data["driver_driver_id"],
        # "pickup_location": data["pickup_location"],
        # "drop_off_location": data["drop_off_location"],
        # "ride_start_date_time": data["ride_start_date_time"],
        # "ride_end_date_time": data["ride_end_date_time"],
        "booking_details": data,
        "estimated_fare_amount": estimated_fare,
        "estimated_time_arrival": estimated_eta,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
        }
    
    booking_collection.insert_one(booking)
    return jsonify({"message": "Booking created successfully!"}), 201

@bp.route("/get_booking", methods=["GET"])
def get_booking():
    booking_id = request.args.get("booking_id")
    if not booking_id:
        return jsonify({"error": "Booking ID is required"}), 400

    booking = booking_collection.find_one({"_id": ObjectId(booking_id)})
    if not booking:
        return jsonify({"error": "Booking not found"}), 
    
    json_doc = json_util.dumps(booking)

    return Response(json_doc, mimetype='application/json'), 200

@bp.route("/update_booking", methods=["POST"]) # You can use Update function to change the status of the booking
def cancel_booking():
    data = request.get_json()
    booking_collection.update_one(
        {"_id": ObjectId(data["booking_id"])},
        {"$set": {"status": data["status"], "cancellation_reason": data["cancellation_reason"]}} # accept string from frontend for status
    )
    return jsonify({"message": "Booking cancelled!"})


#Calculating the shortest path between two locations
