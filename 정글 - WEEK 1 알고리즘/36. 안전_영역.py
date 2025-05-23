import sys
from collections import deque
import copy
input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

# 맥스 높이 구하기 배열의 가장 큰 값
max_high = []
for i in range(n):
    max_high.append(max(w[i]))
max_high = max(max_high)

max_cnt = 0

for h in range(max_high+1):
    copy_w = copy.deepcopy(w)
    cnt = 0
    
    # 높이에 따른 안전지역 표시
    for i in range(n):
        for j in range(n):
            if w[i][j] <= h:
                copy_w[i][j] = False
            else:
                copy_w[i][j] = True
    
    # BFS로 안전지역 카운트
    for i in range(n):
        for j in range(n):
            if copy_w[i][j]:
                cnt += 1
                queue = deque([(i, j)])
                copy_w[i][j] = False
                
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and copy_w[nx][ny]:
                            copy_w[nx][ny] = False
                            queue.append((nx, ny))
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)

