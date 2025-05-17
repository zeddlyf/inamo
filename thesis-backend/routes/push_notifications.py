from flask import Blueprint, request, jsonify
import requests

bp = Blueprint("push_notifications", __name__)

EXPO_PUSH_URL = "https://exp.host/--/api/v2/push/send"

@bp.route("/send_push_notification", methods=["POST"])
def send_push_notification():
    data = request.get_json()
    payload = {
        "to": data["expo_push_token"],
        "title": data["title"],
        "body": data["message"],
        "sound": "default"
    }
    response = requests.post(EXPO_PUSH_URL, json=payload)
    return jsonify({"message": "Push notification sent!", "status": response.status_code})