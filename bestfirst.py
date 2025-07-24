import heapq

# Define the graph as an adjacency list
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': [],
    'D': ['G'],
    'E': ['G'],
    'G': []
}

# Heuristic values (lower is better; goal node G has 0)
heuristics = {
    'S': 5,
    'A': 4,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 3,
    'G': 0
}

def best_first_search(start, goal):
    visited = set()
    pq = []

    # Push the start node into the priority queue (heuristic, node)
    heapq.heappush(pq, (heuristics[start], start))

    while pq:
        h, current = heapq.heappop(pq)
        print("Visiting Node:", current)

        if current == goal:
            print("Goal Node Found!")
            return

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(pq, (heuristics[neighbor], neighbor))

    print("Goal Node Not Found.")

# Run the Best First Search from S to G
best_first_search('S', 'G')
