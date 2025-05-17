from flask import Blueprint, request, jsonify
from models.transaction_history import transaction_history_collection

bp = Blueprint("transaction_history", __name__)

@bp.route("/get_transactions/<string:wallet_id>", methods=["GET"])
def get_transactions(wallet_id):
    transactions = transaction_history_collection.find({"wallet_wallet_id": wallet_id})
    return jsonify([t for t in transactions])