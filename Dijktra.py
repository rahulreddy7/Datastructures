import sys

graph = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}}


def shortest_path(graph, start, end):
    short_distance = {}
    path = []
    pred = {}
    infinity = sys.maxsize
    all_nodes = graph
    for node in all_nodes:
        short_distance[node] = infinity
    short_distance[start] = 0

    while all_nodes:
        min_node = None
        for node in all_nodes:
            if min_node is None:
                min_node = node
            elif short_distance[node] < short_distance[min_node]:
                min_node = node
        for childnode, weight in graph[min_node].items():
            if short_distance[min_node] + weight < short_distance[childnode]:
                short_distance[childnode] = short_distance[min_node] + weight
                pred[childnode] = min_node
        all_nodes.pop(min_node)

    current_node = end
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = pred[current_node]
        except KeyError:
            print("Path Not found")
            break
    path.insert(0, start)
    if short_distance[end] != infinity:
        print("The shortest distance is " + str(short_distance[end]))
        print("The path is " + str(path))


shortest_path(graph, 'a', 'c')
