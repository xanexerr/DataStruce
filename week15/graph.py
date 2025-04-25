class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def get_edges(self):
        edges = []
        for u in self.graph:
            for v in self.graph[u]:
                if (v, u) not in edges:  # Avoid duplicates
                    edges.append((u, v))
        return edges