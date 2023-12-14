from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming an undirected graph

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_node, path = queue.popleft()

        if current_node == goal:
            print(f"Goal node {goal} found! Path: {path}")
            return True

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    print("Goal node not found.")
    return False

if __name__ == "__main__":
    # Create the graph
    graph = Graph()
    edges = [(1, 3), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 8), (7, 8)]
    for edge in edges:
        graph.add_edge(*edge)
    # BFS from initial node 1 to goal node 8
    initial_node = 1
    goal_node = 8
    bfs(graph.graph, initial_node, goal_node);
