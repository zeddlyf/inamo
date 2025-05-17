from connection import db

class TransactionHistory:
    def __init__(self, wallet_wallet_id, booking_booking_id, transaction_type, amount, transaction_date):
        self.wallet_wallet_id = wallet_wallet_id  # Reference to Wallet ID
        self.booking_booking_id = booking_booking_id  # Reference to Booking ID
        self.transaction_type = transaction_type  # "payment", "top-up", "withdrawal"
        self.amount = amount  # Transaction amount
        self.transaction_date = transaction_date  # Date of the transaction

    def to_dict(self):
        return self.__dict__

# MongoDB Collection
transaction_history_collection = db["transaction_history"]