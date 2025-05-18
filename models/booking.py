from connection import db
import heapq 
import json

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

# from utils import naga_edges_for_mapbox

# # Parse Graph from GEOJSON
# class Dijkstra:

#     with open(naga_edges_for_mapbox) as f:
#         data = json.load(f)
        
#     graph = {}

#     for feature in data['features']:
#         u = feature['properties']['u']
#         v = feature['properties']['v']
#         distance = feature['properties']['length']
        
#         distance = distance / 1000  # Convert to kilometers
        
#         if u not in graph: graph[u] = {}
#         if v not in graph: graph[v] = {}
        
#         graph[u][v] = distance
#         if not feature['properties']['oneway']:
#             graph[v][u] = distance
        
#     # Dijkstra's Algorithm
#     def dijkstra(graph, start, end):
#         queue = [(0, start)]
#         distances = {node: float('inf') for node in graph}
#         distances[start] = 0
#         previous = {}
        
#         while queue:
#             current_distance, current_node = heapq.heappop(queue)
            
#             if current_node == end: break
            
#             for neighbor, weight in graph(current_node, {}).items():
#                 distance = current_distance + weight
                
#                 if distance < distances[neighbor]:
#                     distances[neighbor] = distance
#                     previous[neighbor] = current_node
#                     heapq.heappush(queue, (distance, neighbor))
                    
#         estimated_eta = (distances[end] / 40) * 60  # Assuming an average speed of 40 km/h
#         distance = distances[end]
#         return distance, previous, estimated_eta
        
#     def calculate_fare(distance):
#         base_fare = 15
#         rate_per_km = 11
#         base_km = 1
        
#         if distance <= base_km: return base_fare
#         else: return base_fare + (distance - base_km) * rate_per_km
    