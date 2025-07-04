import sys

def binary(n):
    dp = [0] * (n+2)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 15746
    return dp[n]

n = int(input())

print(binary(n))
# 15746