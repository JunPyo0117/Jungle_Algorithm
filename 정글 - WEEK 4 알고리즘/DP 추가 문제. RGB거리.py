import sys
input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

# i번째 집까지 고려했을 때, j색으로 칠하는 조합
dp = [([0] * 3) for _ in range(n+1)]
dp[1] = rgb[0]

for i in range(2,n+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i-1][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i-1][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i-1][2]

print(dp)
print(min(dp[n]))
