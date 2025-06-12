n = int(input())

# dp[i][j] = 길이가 i이고 마지막 자리가 j인 계단 수의 개수
dp = [[0] * 10 for _ in range(n + 1)]

# 길이가 1인 경우 초기화 (1~9로 시작)
for i in range(1, 10):
    dp[1][i] = 1

# 길이 2부터 n까지 계산
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            # 0으로 끝나는 경우: 이전 자리가 1인 경우만 가능
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            # 9로 끝나는 경우: 이전 자리가 8인 경우만 가능
            dp[i][j] = dp[i-1][8]
        else:
            # 1~8로 끝나는 경우: 이전 자리가 j-1 또는 j+1인 경우
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

# 길이가 n인 모든 계단 수의 합
result = sum(dp[n]) % 1000000000
print(result) 