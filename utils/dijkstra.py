import networkx as nx
import heapq 
import json

class RouteNavigator:
    def __init__(self):
        self.graph = nx.Graph()

    def add_route(self, start, end, distance):
        self.graph.add_edge(start, end, weight=distance)

    def find_shortest_path(self, origin, destination):
        try:
            path = nx.shortest_path(self.graph, source=origin, target=destination, weight="weight")
            distance = nx.shortest_path_length(self.graph, source=origin, target=destination, weight="weight")
            return {"path": path, "distance": distance}
        except nx.NetworkXNoPath:
            return {"error": "No path found"}
        

class Dijkstra:
    def __init__(self):
        with open("utils/naga_edges_for_mapbox.geojson") as f:
            data = json.load(f)

        self.graph = {}

        for feature in data['features']:
            u = feature['properties']['u']
            v = feature['properties']['v']
            distance = feature['properties']['length'] / 1000  # in km

            if u not in self.graph:
                self.graph[u] = {}
            if v not in self.graph:
                self.graph[v] = {}

            self.graph[u][v] = distance
            if not feature['properties']['oneway']:
                self.graph[v][u] = distance

    @staticmethod
    def dijkstra(graph, start, end):
        queue = [(0, start)]
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        previous = {}

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node == end:
                break

            for neighbor, weight in graph.get(current_node, {}).items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))
        print(distances[end])

        estimated_eta = (distances[end] / 40) * 60  # 40 km/h average speed
        distance = distances[end]

        return distance, estimated_eta

    @staticmethod
    def calculate_fare(distance):
        base_fare = 15
        rate_per_km = 11
        base_km = 1

        if distance <= base_km:
            return base_fare
        else:
            return base_fare + (distance - base_km) * rate_per_km


