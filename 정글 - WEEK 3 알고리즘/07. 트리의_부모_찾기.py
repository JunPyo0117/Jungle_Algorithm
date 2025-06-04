import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# DFS로 각 노드의 부모 찾기
def dfs(graph, v, visited, parent):
    visited[v] = True
    
    # 현재 노드와 연결된 다른 노드들 방문
    for next_node in graph[v]:
        if not visited[next_node]:
            parent[next_node] = v  # next_node의 부모는 v
            dfs(graph, next_node, visited, parent)

n = int(input().rstrip())
edges = [list(map(int, input().split())) for _ in range(n-1)]

# 그래프 생성
graph = [[] for _ in range(n+1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
# 각 노드의 부모를 저장할 배열
parent = [0] * (n+1)
visited = [False] * (n+1)

# 루트 노드 1에서 시작해서 DFS 실행
dfs(graph, 1, visited, parent)

# 2번 노드부터 n번 노드까지의 부모 출력
for i in range(2, n+1):
    print(parent[i])