from collections import Counter


N, M = list(map(int, input().split()))
edges = []
all_node_with_edges: dict = {}
for i in range(M):
    A, B = list(map(int, input().split()))
    edges.append((A, B))
    if all_node_with_edges.get(A):
        all_node_with_edges[A] += 1
    else:
        all_node_with_edges[A] = 1

    if all_node_with_edges.get(B):
        all_node_with_edges[B] += 1
    else:
        all_node_with_edges[B] = 1

val = 1
power = N - len(all_node_with_edges)
val *= 3 ** power

values = list(all_node_with_edges.values())
if len(all_node_with_edges) != 0:
    if max(values) >= 3:
        print(0)
        import sys
        sys.exit()

remains = edges.copy()
graphs = []
while len(remains) > 0:
    edge = remains.pop()
    if len(graphs) == 0:
        graphs.append(list(edge))
        continue

    found = False
    for i, graph in enumerate(graphs):
        if edge[0] in graph or edge[1] in graph:
            found = True
            graphs[i].extend(list(edge))

    if not found:
        graphs.append(list(edge))

for graph in graphs:
    elemcount = {}
    for e in graph:
        if elemcount.get(e):
            elemcount[e] += 1
        else:
            elemcount[e] = 1

    values = list(elemcount.values())
    if min(values) == 1:
        val *= 3 * 2 ** (len(values) - 1)
    else:
        val *= 6


print(val)
