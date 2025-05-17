import sys

input = sys.stdin.readline

c = int(input())

for _ in range(c):
    n, *score = map(int, input().split())
    avg = 0
    avg = sum(score)/n
    cnt = 0
    rate = 0
    # print(avg)
    for i in score:
        if avg < i:
            cnt += 1
    rate = (cnt / n) * 100
    # print(rate)
    print("{:.3f}".format(rate)+"%")