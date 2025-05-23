# 부분수열의 합 3
from itertools import combinations
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
num_list = list(map(int, input().split()))
# print(num_list)
cnt = 0


for i in range(n):
    for j in combinations(num_list, i):
        if sum(j) == s:
            cnt += 1

print(cnt)
