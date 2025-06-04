import sys
import heapq
from collections import deque
input = sys.stdin.readline

def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end=' ')

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for a,b in edges:
    graph[a].append(b)
    indegree[b] += 1

topology_sort()