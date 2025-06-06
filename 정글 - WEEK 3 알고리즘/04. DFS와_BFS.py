import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True

    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


# 입력값
n, m, v = map(int, input().split())
# 간선 리스트 받기 
m_list = [list(map(int, input().split())) for _ in range(m)]
# 인접 리스트 초기화
graph = [[] for _ in range(n + 1)]

# 간선 리스트 -> 인접 리스트로 변환
for a, b in m_list:
    graph[a].append(b)
    graph[b].append(a)

# 인접리스트 정렬
# "정점 번호가 작은 것을 먼저 방문" 조건을 만족하려면 인접 리스트가 정렬되어 있어야 함
for i in range(1, n + 1):
    graph[i].sort()

visited_dfs = [False] * (n+1)
dfs(graph, v, visited_dfs)
print()
visited_bfs = [False] * (n+1)
bfs(graph, v, visited_bfs)

# # dfs 알고리즘 
# def dfs(graph, v, visited):
#     # 노드 방문 처리
#     visited[v] = True
#     print(v, end=' ')
#     # 현재 노드와 연결된 다른 노드들 재귀적을 방문 
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# def bfs(graph, start, visited):
#     # bfs는 큐를 사용하기 때문에 큐 라이브러리 사용
#     queue = deque([start])
#     # 노드 방문 처리
#     visited[start] = True
#     # 큐가 빌때까지 반복 
#     while queue:
#         # 큐에 원소하나를 뽑아 출력 (방문한 곳)
#         v = queue.popleft()
#         print(v, end=' ')
#         # 아직 방문하지 않은 인접 노드들을 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# # 입력값
# n, m, v = map(int, input().split())
# # 간선 리스트 받기 
# m_list = [list(map(int, input().split())) for _ in range(m)]
# # 인접 리스트 초기화
# graph = [[] for _ in range(n + 1)]

# # 간선 리스트 -> 인접 리스트로 변환
# for a, b in m_list:
#     graph[a].append(b)
#     graph[b].append(a)
# print(graph)
# # 인접리스트 정렬
# # "정점 번호가 작은 것을 먼저 방문" 조건을 만족하려면 인접 리스트가 정렬되어 있어야 함
# for i in range(1, n + 1):
#     graph[i].sort()
# # print(graph)

# # dfs visited 초기화 
# visited_dfs = [False] * (n+1)
# dfs(graph, v, visited_dfs)
# print()
# # bfs visited 초기화 
# visited_bfs = [False] * (n+1)
# bfs(graph, v, visited_bfs)
# print()