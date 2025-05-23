import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
d = deque(range(1, n+1))
yo = []


for _ in range(n):
    d.rotate(-k+1)
    yo.append(d.popleft())
    

print("<" + ', '.join(map(str, yo)) + ">")

