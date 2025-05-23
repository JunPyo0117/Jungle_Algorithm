import sys
from itertools import permutations
input = sys.stdin.readline


def maximum(arr):

    num_list = []
    for i in permutations(arr, len(arr)):
        max_num = 0
        for j in range(len(i)-1):
            max_num += abs(i[j] - i[j+1])
            num_list.append(max_num)


    return num_list



n = int(input())

arr = list(map(int, input().split()))

print(max(maximum(arr)))

