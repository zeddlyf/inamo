from connection import db

class Commuter:
    def __init__(self, user_user_id, valid_id):
        self.user_user_id = user_user_id  # Reference to User ID
        self.valid_id = valid_id  # Government-issued ID

    def to_dict(self):
        return self.__dict__

# MongoDB Collection
commuter_collection = db["commuters"]