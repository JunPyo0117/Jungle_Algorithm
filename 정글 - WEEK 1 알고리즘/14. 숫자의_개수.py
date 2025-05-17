import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

num_cnt = [0] * 10
multi = 0
multi = str(a*b*c)

for i in multi:
    i = int(i)
    num_cnt[i] += 1

for j in num_cnt:
    print(j)