import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [ int(input()) for _ in range(n)]
coins.reverse()

cnt = 0

for coin in coins:
    cnt += k//coin
    k %= coin

print(cnt)
