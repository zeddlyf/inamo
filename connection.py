import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["Eyytrike"]

# def check_connection():
#     try:
#         # Attempt to get server information
#         client.server_info()
#         print("MongoDB connection successful.")
#     except Exception as e:
#         print(f"MongoDB connection failed: {e}")
#         return False
#     return True

# check_connection()
