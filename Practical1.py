from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while(queue):
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            print(current)
            for neighbour in graph[current]:
                if neighbour not in visited:
                    queue.append(neighbour)

# def dfs(graph, start):
#     visited = set()
#     stack = [start]
#     while(stack):
#         current = stack.pop()
#         if current not in visited:
#             visited.add(current)
#             print(current)

#             for neighbour in graph[current]:
#                 if neighbour not in visited:
#                     stack.append(neighbour)

def dfs(graph, start, visited = None):
    if visited == None:
        visited = set()
    print(start)
    visited.add(start)
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

bfs(graph,'A')
print('#################')
dfs(graph, 'A')