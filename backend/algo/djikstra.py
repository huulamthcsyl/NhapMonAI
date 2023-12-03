from collections import defaultdict, deque
from heapq import heappop, heappush


class Graph:
    def __init__(self, G):
        self.graph = defaultdict(list)
        self.G = G
        for u, v, attrs in list(G.edges.data()):
            self.addEdge(u, v, attrs["length"])

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

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
            path.appendleft((self.G.nodes[end]["y"], self.G.nodes[end]["x"]))
            end = trace[end]
        path.appendleft((self.G.nodes[start]["y"], self.G.nodes[start]["x"]))
        return path
