import sys
import copy
input = sys.stdin.readline

def Dwarfs(arr):
    dwarfs_tall = 100
    
    for i in range(len(arr)):
        temp_arr = copy.deepcopy(arr)
        temp_arr.pop(i)
        for j in range(len(temp_arr)):
            temp_arr2 = copy.deepcopy(temp_arr)
            temp_arr2.pop(j)
            if sum(temp_arr2) == dwarfs_tall:
                return sorted(temp_arr2)

arr = [int(input()) for _ in range(9)]

print('\n'.join(map(str, Dwarfs(arr))))