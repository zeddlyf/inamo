from connection import db

class Booking:
    def __init__(self, commuter_commuter_id, driver_driver_id, pickup_location, drop_off_location,
                 ride_start_date_time, ride_end_date_time, estimated_fare_amount, actual_fare_amount,
                 status, cancellation_reason, promo_code, created_at, updated_at):
        self.commuter_commuter_id = commuter_commuter_id  # Reference to Commuter ID
        self.driver_driver_id = driver_driver_id  # Reference to Driver ID
        self.pickup_location = pickup_location
        self.drop_off_location = drop_off_location
        self.ride_start_date_time = ride_start_date_time
        self.ride_end_date_time = ride_end_date_time
        self.estimated_fare_amount = estimated_fare_amount
        self.actual_fare_amount = actual_fare_amount
        self.status = status  # "pending", "completed", "cancelled"
        self.cancellation_reason = cancellation_reason
        self.promo_code = promo_code
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return self.__dict__

# MongoDB Collection
booking_collection = db["bookings"]