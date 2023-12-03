from flask import Flask, request
import osmnx as ox
from flask_cors import CORS
import sys
from algo.nearest_node import nearest_node
from algo.djikstra import Graph

app = Flask(__name__)
CORS(app)


def solve(start, end):
    G = ox.graph_from_place("Hoàn Kiếm, Hà Nội, Vietnam", network_type="drive")
    coords = [(data["y"], data["x"], key) for key, data in G.nodes(data=True)]
    nr_start = nearest_node((start["lat"], start["lng"]), coords)
    nr_end = nearest_node((end["lat"], end["lng"]), coords)
    graph = Graph(G)
    path = graph.dijkstra(nr_start, nr_end)
    path.appendleft((start["lat"], start["lng"]))
    path.append((end["lat"], end["lng"]))
    return list(path)


@app.route("/")
def index():
    m1 = {
        "lat": float(request.args.get("m1_lat")),
        "lng": float(request.args.get("m1_lng")),
    }
    m2 = {
        "lat": float(request.args.get("m2_lat")),
        "lng": float(request.args.get("m2_lng")),
    }
    return solve(m1, m2)


app.run(debug=True)
