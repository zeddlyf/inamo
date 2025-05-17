from connection import db

class Driver:
    def __init__(self, user_user_id, drivers_license):
        self.user_user_id = user_user_id  # Reference to User ID
        self.drivers_license = drivers_license  # License document

    def to_dict(self):
        return self.__dict__

# MongoDB Collection
driver_collection = db["drivers"]