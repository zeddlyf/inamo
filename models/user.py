from connection import db

class User:
    def __init__(self, type, email_address, mobile_number, password, first_name, last_name, middle_name=None, created_at=None, updated_at=None):
        self.type = type
        self.email_address = email_address
        self.mobile_number = mobile_number
        self.password = password
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return self.__dict__

user_collection = db["users"]