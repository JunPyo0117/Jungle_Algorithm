import sys
# 백준의 재귀 호출 한계는 1000, dfs로 풀려면 제한을 해제해줘야만 가능함
sys.setrecursionlimit(10**5)
n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
max_num = 0
for i in range(n):
    tmp = max(area[i])
    if max_num < tmp:
        max_num = tmp

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if not visited[x][y]:
        visited[x][y] = 1
        # 상하좌우 모두 방문 하도록
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

max_cnt = 0

for rain in range(max_num):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] <= rain:
                visited[i][j] = 1
    for i in range(n):
        for j in range(n):
            if dfs(i, j):
                cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
        
print(max_cnt)