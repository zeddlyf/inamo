from flask import Blueprint, request, jsonify
from models.payment import payment_collection

bp = Blueprint("payment", __name__)

@bp.route("/process_payment", methods=["POST"])
def process_payment():
    data = request.get_json()
    payment_collection.insert_one(data)
    return jsonify({"message": "Payment processed successfully!"})