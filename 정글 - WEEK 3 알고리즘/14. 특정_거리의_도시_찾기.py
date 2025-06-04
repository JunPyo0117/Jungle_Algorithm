import sys
import heapq
from collections import deque
input = sys.stdin.readline
INF = float('inf')

def djikstra(start, graph):
    q = []

    heapq.heappush(q, (0, start))
    dist_table[start] = 0

    while q:
        i_dist, i = heapq.heappop(q)    
        
        if i_dist > dist_table[i]:
            continue

        # i의 인접 노드 j 확인
        for j, j_dist in graph[i]:
            # j: 인접 노드, j_dist: 간선 가중치
            # 현재 노드를 거쳐, 인접 노드로 이동하는 거리
            new_dist = i_dist + j_dist

            # 거리가 더 짧으면 갱신
            if new_dist < dist_table[j]:
                dist_table[j] = new_dist
                heapq.heappush(q, (new_dist, j))



# 도시 수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x= map(int, input().split())
# A,B
road = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
dist_table = [INF] * (n+1)

# a에서 b로 가는 튜플 추가(도착 도시, 비용) 
for a, b in road:
    graph[a].append((b, 1))

# print(graph)
djikstra(x, graph)

# print(dist_table)

found = False
for idx, cost in enumerate(dist_table):
    if cost == k:
        print(idx)
        found = True

if not found:
    print(-1)