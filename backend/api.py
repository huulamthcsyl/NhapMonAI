from flask import Flask, request
from flask_cors import CORS
from algo.graph import Graph
import pickle

app = Flask(__name__)
CORS(app)
with open("graph.pkl", "rb") as f:
    g: Graph = pickle.load(f)


def solve(g: Graph, start, end):
    nearest_start_id = g.nearest_node((start["lat"], start["lng"]))
    nearest_end_id = g.nearest_node((end["lat"], end["lng"]))
    path = g.dijkstra(nearest_start_id, nearest_end_id)
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
    return solve(g, m1, m2)


app.run(debug=True)
