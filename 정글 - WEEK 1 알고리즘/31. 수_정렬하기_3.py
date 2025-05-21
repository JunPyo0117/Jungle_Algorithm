import sys

input = sys.stdin.readline

n = int(input())
counting = [0] * 10001

for _ in range(n):
    num = int(input())
    counting[num] += 1

for i in range(len(counting)):
    if counting[i] != 0:
        for _ in range(counting[i]):
            print(i)

