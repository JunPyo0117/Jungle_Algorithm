import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs():
    water_q = deque()      # 물용 큐
    hedgehog_q = deque()   # 고슴도치용 큐
    biber_x = 0
    biber_y = 0

    # 배열 먼저 선언
    visited = [[False] * c for _ in range(r)]
    distance = [[0] * c for _ in range(r)]  # 거리 저장용

    for i in range(r):
        for j in range(c):
            if forest[i][j] == 'S':
                hedgehog_q.append((i, j))
                visited[i][j] = True 
                distance[i][j] = 0  
            elif forest[i][j] == '*':  # 물 찾기!
                water_q.append((i, j))
            elif forest[i][j] == 'D':
                biber_x, biber_y = i, j

    time = 0
    while hedgehog_q:  # 고슴도치가 있는 동안
        
        # 1단계: 물 확산 먼저!
        for _ in range(len(water_q)):  # 현재 물들만 확산
            x, y = water_q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < r and 0 <= ny < c and (forest[nx][ny] == '.' or forest[nx][ny] == 'S'):
                    forest[nx][ny] = '*'  # 물로 변경!
                    water_q.append((nx, ny))
        
        # 2단계: 고슴도치 이동
        next_hedgehog_q = deque()
        while hedgehog_q:
            x, y = hedgehog_q.popleft()
            
            # 4방향 이동...
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or ny < 0 or nx >= r or ny >= c:
                    continue

                # 비버 굴 도착 체크
                if nx == biber_x and ny == biber_y:
                    return time + 1

                if not visited[nx][ny] and forest[nx][ny] != 'X' and forest[nx][ny] != '*':
                    visited[nx][ny] = True
                    next_hedgehog_q.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1

        hedgehog_q = next_hedgehog_q
        time += 1

    return "KAKTUS"  # 도달 불가능한 경우
   
r, c = map(int, input().split())
forest = [list(input().rstrip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())
