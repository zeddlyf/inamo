from flask import Blueprint, request, jsonify
from models.driver import driver_collection

bp = Blueprint("driver", __name__)

@bp.route("/register_driver", methods=["POST"])
def register_driver():
    data = request.get_json()
    driver_collection.insert_one(data)
    return jsonify({"message": "Driver registered successfully!"})