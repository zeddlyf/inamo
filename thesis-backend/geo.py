import osmnx as ox

G = ox.graph_from_place("Naga City, Camarines Sur, Philippines", network_type="drive")

geojson = ox.io.save_graph_geojson(G, filepath="naga_city_roads.geojson")