import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

EXPO_PUSH_TOKEN = os.getenv("EXPO_PUSH_TOKEN")

MAPBOX_ACCESS_TOKEN = os.getenv("MAPBOX_ACCESS_TOKEN")

FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

FLASK_ENV = os.getenv("FLASK_ENV", "development")

FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"