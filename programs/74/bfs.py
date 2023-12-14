from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start_node, end_node):
        # Add edges for an undirected graph
        if start_node not in self.graph:
            self.graph[start_node] = []
        if end_node not in self.graph:
            self.graph[end_node] = []
        self.graph[start_node].append(end_node)
        self.graph[end_node].append(start_node)

    def display_graph(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")

def bfs(graph, start, goal):
    if start not in graph or goal not in graph:
        return []

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return []

# Example Usage:
# Create an undirected graph and add edges
g = Graph()
g.add_edge('1', '2')
g.add_edge('1', '3')
g.add_edge('2', '4')
g.add_edge('2', '5')
g.add_edge('3', '6')
g.add_edge('3', '7')
g.add_edge('4', '8')
g.add_edge('5', '8')
g.add_edge('6', '8')
g.add_edge('7', '8')

# Display the graph
g.display_graph()

# Perform BFS from node '1' to '8'
initial_node = '1'
goal_node = '8'
result_path = bfs(g.graph, initial_node, goal_node)

# Display the result
if result_path:
    print(f"Path from {initial_node} to {goal_node}: {result_path}")
else:
    print(f"No path found from {initial_node} to {goal_node}")

