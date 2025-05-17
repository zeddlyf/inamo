from flask import Flask
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from dotenv import load_dotenv
import os
from connection import db
from routes.auth import bp as auth_bp
from routes.commuter import bp as commuter_bp
from routes.driver import bp as driver_bp
from routes.wallet import bp as wallet_bp
from routes.payment import bp as payment_bp
from routes.transaction_history import bp as transaction_history_bp
from routes.booking import bp as booking_bp
from routes.navigation import bp as navigation_bp
from routes.push_notifications import bp as push_notifications_bp

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600  # 1 hour
app.config["JWT_BLACKLIST_ENABLED"] = True
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access"]

# Setup JWT authentication
jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token = db.token_blacklist.find_one({"jti": jti})
    return token is not None

# Setup WebSockets
socketio = SocketIO(app, cors_allowed_origins="*")

# Register API Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(commuter_bp, url_prefix="/commuter")
app.register_blueprint(driver_bp, url_prefix="/driver")
app.register_blueprint(wallet_bp, url_prefix="/wallet")
app.register_blueprint(payment_bp, url_prefix="/payment")
app.register_blueprint(transaction_history_bp, url_prefix="/transactions")
app.register_blueprint(booking_bp, url_prefix="/booking")
app.register_blueprint(navigation_bp, url_prefix="/navigation")
app.register_blueprint(push_notifications_bp, url_prefix="/notifications")

# Ensure MongoDB connection is alive
@app.before_request
def connect_db():
    db.client.server_info()

# Start WebSocket server
if __name__ == "__main__":
    socketio.run(host="0.0.0.0", port=5000, debug=True)
