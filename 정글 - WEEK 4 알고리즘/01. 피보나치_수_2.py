import sys

n = int(input())

# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibo(n-1) + fibo(n-2)

# print(fibo(n))

# def fibo(n):
#     a, b = 0, 1
#     for i in range(2, n+1):
#         a, b = b, a+b
#     return b

def dp_fibo(n):
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n]


print(dp_fibo(n))