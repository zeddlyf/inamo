from connection import db

class Payment:
    def __init__(self, wallet_wallet_id, booking_booking_id, amount_paid, promo_discount, created_at):
        self.wallet_wallet_id = wallet_wallet_id  # Reference to Wallet ID
        self.booking_booking_id = booking_booking_id  # Reference to Booking ID
        self.amount_paid = amount_paid  # Total payment made
        self.promo_discount = promo_discount  # Discount applied
        self.created_at = created_at  # Timestamp of payment

    def to_dict(self):
        return self.__dict__

# MongoDB Collection
payment_collection = db["payments"]