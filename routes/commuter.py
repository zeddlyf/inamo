from flask import Blueprint, request, jsonify
from models.commuter import commuter_collection

bp = Blueprint("commuter", __name__)

@bp.route("/register_commuter", methods=["POST"])
def register_commuter():
    data = request.get_json()
    commuter_collection.insert_one(data)
    return jsonify({"message": "Commuter registered successfully!"})