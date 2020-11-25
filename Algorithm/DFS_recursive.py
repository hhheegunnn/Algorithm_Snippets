# dfs 재귀

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [False]*9

result = []

def dfs_recursive(graph,start_node,visited):
    visited[start_node] = True
    result.append(start_node)
    for node in graph[start_node]:
        if not visited[node]:
            dfs_recursive(graph,node,visited)

    return result


print("dfs_recursive = ", dfs_recursive(graph,1,visited))
# 1 2 7 6 8 3 4 5



