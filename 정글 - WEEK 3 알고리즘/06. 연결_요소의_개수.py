import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(graph, v, visited):
    # 노드 방문 처리
    visited[v] = True
    # print(v, end=' ')
    # 현재 노드와 연결된 다른 노드들 재귀적을 방문 
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m = map(int, input().split())
# 간선 리스트 받기 
m_list = [list(map(int, input().split())) for _ in range(m)]

# 인접 리스트 초기화
graph = [[] for _ in range(n + 1)]

for a, b in m_list:
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

visited_dfs = [False] * (n+1)
count = 0  # 연결 요소 개수
for i in range(1, n+1):  
    if not visited_dfs[i]:  
        dfs(graph, i, visited_dfs)  
        count += 1

print(count)