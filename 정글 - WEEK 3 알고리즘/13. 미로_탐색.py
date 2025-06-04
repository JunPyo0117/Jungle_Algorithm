import sys
import heapq
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    q = deque()
    q.append((x,y))

    # 큐가 없어질 때 까지
    while q:
        # x, y 언패킹
        x, y = q.popleft()

        # 상 하 좌 우 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖으로 벗어날 때 그대로 진행
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            # 벽을 만났을 때 그대로 진행
            if graph[nx][ny] == 0:
                continue
            
            # 길을 찾으면 해당 길마다 1 씩 증가
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    return graph[n-1][m-1] # 도착지의 끝 점
        
# n x m 행렬
n, m = map(int, input().split())
# 계행문자 제거 후 리스트
graph = [list(map(int, input().rstrip())) for _ in range(n)]
# print(graph)

# 상, 하, 좌, 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))