import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)

    for j in s:
        print(j*r, end="")
    print()