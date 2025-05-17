from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt, get_jwt_identity
from models.user import user_collection
from datetime import datetime
from connection import db

bp = Blueprint("auth", __name__)

# Create a collection for blacklisted tokens
token_blacklist = db.token_blacklist

@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    hashed_pw = generate_password_hash(data["password"])
    user_data = {**data, "password": hashed_pw}

    # Conditioning for organizing user types
    # if "user_type" is "driver":
    #     user_data["user_type"] = "commuter"  # Default user type

    user_collection.insert_one(user_data)
    return jsonify({"message": "User registered successfully!"})

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = user_collection.find_one({"email_address": data["email_address"]})
    
    if user and check_password_hash(user["password"], data["password"]):
        token = create_access_token(identity=str(user["_id"]))
        return jsonify({"access_token": token, "user_type": user["user_type"]})
    
    return jsonify({"message": "Invalid credentials"}), 401

@bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    now = datetime.utcnow()
    token_blacklist.insert_one({
        "jti": jti,
        "created_at": now
    })
    return jsonify({"message": "Successfully logged out"}), 200