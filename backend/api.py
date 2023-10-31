from flask import Flask, request
from flask_restful import Resource, Api
import osmnx as ox
from flask_cors import CORS
import sys

app = Flask(__name__)
CORS(app)

def solve(orig, dest):
    G = ox.graph_from_place("Hoàn Kiếm, Hà Nội, Vietnam", network_type='drive')
    orig_node = ox.nearest_nodes(G, orig['lng'], orig['lat'])
    dest_node = ox.nearest_nodes(G, dest['lng'], dest['lat'])
    routes = ox.shortest_path(G, orig_node, dest_node)
    coordinates = [(float(G.nodes[i]['y']), float(G.nodes[i]['x'])) for i in routes]
    coordinates.insert(0, (orig['lat'], orig['lng']))
    coordinates.append((dest['lat'], dest['lng']))
    return coordinates

@app.route("/")
def index():
    m1 = {'lat': float(request.args.get('m1_lat')), 'lng': float(request.args.get('m1_lng'))}
    m2 = {'lat': float(request.args.get('m2_lat')), 'lng': float(request.args.get('m2_lng'))}
    return solve(m1, m2)

app.run(debug=True)