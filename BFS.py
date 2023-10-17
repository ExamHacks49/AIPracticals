from collections import deque

# Define the graph as a dictionary of lists
graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

# Define the BFS function
def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the starting node

    while queue:  # Loop until the queue is empty
        vertex = queue.popleft()  # Get the next vertex from the queue

        if vertex not in visited:
            visited.add(vertex)  # Mark the vertex as visited
            print(vertex)

            # Add all adjacent vertices to the queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Call the BFS function with the starting node
bfs(graph, 'A')
