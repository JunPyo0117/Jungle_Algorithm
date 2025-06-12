import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = triangle[0][0]

for i in range(n+1):
    for j in range(n+1):
        dp[i][j] = 1

