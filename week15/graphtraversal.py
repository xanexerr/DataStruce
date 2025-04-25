class graphtraversal:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()

    def dfs(self, node):
        if node not in self.visited:
            print(node)
            self.visited.add(node)
            for neighbor in self.graph[node]:
                self.dfs(neighbor)

    def bfs(self, start):
        queue = [start]
        self.visited.add(start)
        while queue:
            node = queue.pop(0)
            print(node)
            for neighbor in self.graph[node]:
                if neighbor not in self.visited:
                    queue.append(neighbor)
                    self.visited.add(neighbor)
                    
                    
print("Graph Traversal")
# print("DFS")
# print("BFS")
# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

traversal = graphtraversal(graph)
traversal.dfs('A')
traversal.visited.clear()  # Clear visited for BFS