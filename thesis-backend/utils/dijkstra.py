import networkx as nx

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