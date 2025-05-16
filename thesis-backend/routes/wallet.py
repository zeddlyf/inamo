from flask import Blueprint, request, jsonify
from models.wallet import wallet_collection

bp = Blueprint("wallet", __name__)

@bp.route("/create_wallet", methods=["POST"])
def create_wallet():
    data = request.get_json()
    wallet_collection.insert_one(data)
    return jsonify({"message": "Wallet created successfully!"})

@bp.route("/update_balance", methods=["POST"])
def update_balance():
    data = request.get_json()
    wallet_collection.update_one(
        {"user_user_id": data["user_user_id"]}, 
        {"$set": {"balance": data["balance"]}}
    )
    return jsonify({"message": "Balance updated!"})