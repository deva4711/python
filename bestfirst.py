import heapq


graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': [],
    'D': ['G'],
    'E': ['G'],
    'G': []
}


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
best_first_search('S', 'G')
