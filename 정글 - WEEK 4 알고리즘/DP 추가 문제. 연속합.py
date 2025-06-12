import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

dp = [0] * (n)
dp[0] = n_list[0]
minus = max(n_list)

# for i in range(1, n+1):
#     if dp[i-1] + n_list[i-1] < n_list[i-1]:
#         dp[i] = n_list[i-1]
#     else:
#         dp[i] = dp[i-1] + n_list[i-1]

for i in range(1, n):
    dp[i] = max(dp[i-1] + n_list[i], n_list[i])

# if minus < 0:
#     print(minus)
# else:
print(max(dp))