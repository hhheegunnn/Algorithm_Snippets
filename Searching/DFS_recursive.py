# dfs 재귀

graph = [[1,2],[0,3,4],[0,5,6],[1],[1],[2],[2]]

visited = [False]*7

result = []

def dfs_recursive(graph,start_node,visited):
    visited[start_node] = True
    result.append(start_node)
    for node in graph[start_node]:
        if not visited[node]:
            dfs_recursive(graph,node,visited)

    return result


print("dfs_recursive = ", dfs_recursive(graph,0,visited))
# dfs_recursive =  [0, 1, 3, 4, 2, 5, 6]



