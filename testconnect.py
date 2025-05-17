import pymongo

try:
    client = pymongo.MongoClient("mongodb+srv://Etrike:eyytrike2@cluster0.echmkay.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    client.server_info()  # This will raise an exception if the connection fails
    print("MongoDB connection successful.")
except Exception as e:
    print(f"MongoDB connection failed: {e}")
    # Handle the error as needed, e.g., exit the script or retry the connection