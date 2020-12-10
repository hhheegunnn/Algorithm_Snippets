# bfs

from collections import deque

graph = [[1,2],[0,3,4],[0,5,6],[1],[1],[2],[2]]

visited = [False]*7

result = []

def bfs(graph,start_node,visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start_node])
    # 현재 노드를 방문 처리
    visited[start_node] = True
    # 큐가 빌 때까지 반복

    while queue:
    # 큐에서 하나의 원소를 뽑아 출력하기
        node = queue.popleft()
        result.append(node)

    # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return result

print("bfs =", bfs(graph, 0, visited))
# bfs = [0, 1, 2, 3, 4, 5, 6]

