def tsp_dp_with_path(graph):
    n = len(graph)
    memo = {}

    def visit(city, visited):
        if (city, visited) in memo:
            return memo[(city, visited)]

        if visited == (1 << n) - 1:
            return graph[city][0], [0] 

        min_cost = float('inf')
        best_path = []

        for next_city in range(n):
            if not (visited & (1 << next_city)):
                cost, sub_path = visit(next_city, visited | (1 << next_city))
                total_cost = graph[city][next_city] + cost
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_path = [next_city] + sub_path

        memo[(city, visited)] = (min_cost, best_path)
        return memo[(city, visited)]

    total_cost, path = visit(0, 1 << 0)
    complete_path = [0] + path
    return total_cost, complete_path


graph = [
    [0, 12, 13, 14],
    [17, 0, 16, 15],
    [18, 19, 0, 20],
    [23, 22, 21, 0]
]

cost, path = tsp_dp_with_path(graph)

print("Minimum cost:", cost)
print("Optimal path:", path)
