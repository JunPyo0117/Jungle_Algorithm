import sys
input = sys.stdin.readline

# dfs 알고리즘 
def dfs(graph, v, visited):
    global cnt
    # 노드 방문 처리
    visited[v] = True
    if visited[v]:
        cnt += 1
    # print(v, end=' ')
    # 현재 노드와 연결된 다른 노드들 재귀적을 방문 
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n = int(input().rstrip())
m = int(input().rstrip())
# 간선 리스트 받기 
m_list = [list(map(int, input().split())) for _ in range(m)]
# 인접 리스트 초기화
graph = [[] for _ in range(n + 1)]
# print(m_list)
# 간선 리스트 -> 인접 리스트로 변환
for a, b in m_list:
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
# 인접리스트 정렬

# "정점 번호가 작은 것을 먼저 방문" 조건을 만족하려면 인접 리스트가 정렬되어 있어야 함
# for i in range(1, n + 1):
#     graph[i].sort()
# print(graph)

cnt = 0

# dfs visited 초기화 
visited_dfs = [False] * (n+1)
dfs(graph, 1, visited_dfs)
print(cnt-1)

