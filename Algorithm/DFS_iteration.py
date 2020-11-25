# dfs 반복

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [False]*9

result = []

def dfs_iteration(graph,start_node,visited):
    # dfs는 stack, bfs는 queue개념을 이용한다.
    stack = [start_node]
    
    while stack: #스택에 남은것이 없을 때까지 반복
        node = stack.pop() # node : 현재 방문하고 있는 꼭지점
        #현재 node가 방문한 적 없다 -> visited에 추가한다.
        #그리고 해당 node의 자식 node들을 stack에 추가한다.
        if not visited[node]:
            visited[node] = True
            result.append(node)
            stack.extend(graph[node])
    
    return result

print("dfs_iteration = ", dfs_iteration(graph,1,visited))
# 1 8 7 6 2 3 5 4