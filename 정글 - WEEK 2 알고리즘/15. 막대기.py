import sys
input = sys.stdin.readline

n = int(input())

d = [int(input()) for _ in range(n)]
cnt = 0
max_height = 0


for h in reversed(d):
    if h > max_height:
        cnt += 1
        max_height = h

print(cnt)
