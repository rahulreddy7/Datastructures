import collections

def bfs(graph,root):
    visited=set()
    queue=collections.deque([root])
    while queue:
        vertex=queue.popleft()
        display(vertex)
        for node in graph[vertex]:
            if vertex not in visited:
                visited.add(node)
                queue.append(node)

def display(vertex):
    print(vertex)

if __name__=='__main__':
    graph = {0: [1, 2,3], 1: [2], 2: [3], 3:[1]}
    bfs(graph, 0)