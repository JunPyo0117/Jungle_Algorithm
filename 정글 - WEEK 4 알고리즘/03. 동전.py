import sys
input = sys.stdin.readline

def dynamic(coin, amount):
    dp = [0] * (amount+1)
    dp[0] = 1
    for c in coin:
        for i in range(c, amount+1):
            dp[i] += dp[i-c]
    # print(dp)
    return dp[amount]


t = int(input())

for _ in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    amount = int(input())
    print(dynamic(coin, amount))
    

