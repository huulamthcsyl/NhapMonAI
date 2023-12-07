from collections import defaultdict, deque
from heapq import heappop, heappush
from .distance import distance


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.id_node = 0
        self.d = {}
        self.coords = {}
        self.check = defaultdict(bool)

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

    def get_id(self, x, y):
        if (x, y) not in self.d:
            self.d[(x, y)] = self.id_node
            self.id_node += 1
        self.coords[self.d[(x, y)]] = (x, y)
        return self.d[(x, y)]

    def dijkstra(self, start, end):
        visited = defaultdict(bool)
        dist = defaultdict(lambda: float("inf"))
        trace = defaultdict(int)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            _, node = heappop(pq)
            if visited[node]:
                continue
            visited[node] = True
            if node == end:
                break
            for neighbor, weight in self.graph[node]:
                if dist[neighbor] > dist[node] + weight:
                    dist[neighbor] = dist[node] + weight
                    trace[neighbor] = node
                    heappush(pq, (dist[neighbor], neighbor))
        path = deque()
        while end != start:
            path.appendleft((self.coords[end][1], self.coords[end][0]))
            end = trace[end]
        path.appendleft((self.coords[start][1], self.coords[start][0]))
        return path

    def nearest_node(self, point):
        dist = float("inf")
        nearest_node_id = None
        lat, long = point
        for x, y in self.coords.values():
            d = distance(lat, long, y, x)
            if d < dist:
                dist = d
                nearest_node_id = self.d[(x, y)]
        return nearest_node_id
