from flask import Blueprint, request, jsonify
from config import gmaps

bp = Blueprint("eta", __name__)

@bp.route("/calculate_eta", methods=["POST"])
def calculate_eta():
    data = request.get_json()
    origin = data["origin"]
    destination = data["destination"]

    directions = gmaps.directions(origin, destination, mode="driving")
    if directions:
        eta = directions[0]["legs"][0]["duration"]["text"]
        return jsonify({"eta": eta})
    
    return jsonify({"message": "Unable to calculate ETA"}), 400