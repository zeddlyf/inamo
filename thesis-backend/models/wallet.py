from connection import db

class Wallet:
    def __init__(self, user_user_id, balance, top_up_limit, withdrawal_limit, otp_verification, created_at, updated_at):
        self.user_user_id = user_user_id  # Reference to User ID
        self.balance = balance  # Decimal balance amount
        self.top_up_limit = top_up_limit  # Max amount allowed for top-ups
        self.withdrawal_limit = withdrawal_limit  # Max withdrawal limit
        self.otp_verification = otp_verification  # OTP verification for transactions
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return self.__dict__

# MongoDB Collection
wallet_collection = db["wallets"]