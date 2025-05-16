from flask import Blueprint, jsonify, request
from flask_socketio import emit
from main import socketio

bp = Blueprint("notifications", __name__)

@socketio.on("ride_status_update")
def ride_status_update(data):
    emit("ride_status", data, broadcast=True)

@bp.route("/send_notification", methods=["POST"])
def send_notification():
    data = request.get_json()
    socketio.emit("ride_status", data, broadcast=True)
    return jsonify({"message": "Notification sent!"})