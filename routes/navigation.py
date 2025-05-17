import requests
from flask import Blueprint, request, jsonify
from config import MAPBOX_ACCESS_TOKEN

bp = Blueprint("navigation", __name__)

MAPBOX_DIRECTIONS_URL = "https://api.mapbox.com/directions/v5/mapbox/driving"

@bp.route("/get_route", methods=["POST"])
def get_route():
    data = request.get_json()
    origin = f"{data['origin_lng']},{data['origin_lat']}"
    destination = f"{data['destination_lng']},{data['destination_lat']}"

    url = f"{MAPBOX_DIRECTIONS_URL}/{origin};{destination}?access_token={MAPBOX_ACCESS_TOKEN}&geometries=geojson"
    response = requests.get(url)

    if response.status_code == 200:
        route_data = response.json()
        return jsonify(route_data)
    
    return jsonify({"message": "Error fetching route from Mapbox"}), 500