N = int(input())
edges = []
for i in range(N - 1):
    edge = tuple(map(lambda x: int(x) - 1, input().split()))
    edge_ = (edge[1], edge[0])
    edges.append(edge)
    edges.append(edge_)


def shortest_path(start: int):
    distances = [float("inf") for _ in range(N)]
    distances[start] = 0
    while True:
        update = False
        for edge in edges:
            if (distances[edge[0]] != float("inf") and
                    distances[edge[1]] > distances[edge[0]] + 1):
                distances[edge[1]] = distances[edge[0]] + 1
                update = True
        if not update:
            break
    return distances


distances = shortest_path(0)
max_distance = max(distances)
max_distance_idx = distances.index(max_distance)

distances = shortest_path(max_distance_idx)

print(max(distances) + 1)
