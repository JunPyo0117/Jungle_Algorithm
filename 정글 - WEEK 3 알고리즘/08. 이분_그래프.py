import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, current_color, color, graph):
    color[node] = current_color

    for i in graph[node]:
        if color[i] == -1:
             if not dfs(i, 1-current_color, color, graph):  # i를 반대색으로
                return False
        elif color[i] == color[node]:  # 같은 색이면
            return False
    return True


k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]
    graph = [[] for _ in range(v+1)]
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    color = [-1] * (v+1) # -1은 노드를 색칠하지 않음

    is_bipartite = True
    for j in range(1, v+1):
        if color[j] == -1:  # 아직 방문하지 않은 노드만 확인
            if not dfs(j, 0, color, graph):  # 항상 0색으로 시작
                is_bipartite = False
                break  # 하나라도 실패하면 즉시 중단

    if is_bipartite:
        print("YES")
    else:
        print("NO")  