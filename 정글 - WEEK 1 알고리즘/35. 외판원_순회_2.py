import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())

w = [list(map(int, input().split())) for _ in range(n)]



for i in range(len(w)):
    for j in range(len(w)):
        if w[i][j] == 0:
            w[i][j] = float("inf")

n_list = list(range(1, n))

cost_list = []

for permu in permutations(n_list, len(n_list)):
    permu = (0,) + permu +(0,)
    cost = 0
    # print(permu)
    # print(permu[0],permu[1],permu[2], permu[3])
    for k in range(len(permu)-1):
        cost += w[permu[k]][permu[k+1]]
        # print(cost)
    cost_list.append(cost)
print(min(cost_list))