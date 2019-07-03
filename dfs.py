
def dfs(graph,key):
    stack=[]
    stack.append(key)
    visited=[]
    while len(stack)!=0:
        vertex = stack.pop()
        for node in graph[vertex]:
            if node not in visited:
                stack.append(node)
        visited.append(vertex)
    return visited


if __name__=='__main__':
    graph={'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
    print(dfs(graph,'A'))