import sys
input = sys.stdin.readline

def dynamic(num_list):
    dp = [1] * n
    
    for i in range(n):
        for j in range(i):
            if num_list[j] < num_list[i]:
                dp[i] = max(dp[i], dp[j] +1)
    return dp

n = int(input())
num_list = list(map(int, input().split()))

print(max(dynamic(num_list))) 

# ==================================================
# 이분 탐색 이용
# import bisect

# x = int(input().)
# arr = list(map(int, input().split()))

# dp = [arr[0]]

# for i in range(x):
#     if arr[i] > dp[-1]:
#         dp.append(arr[i])
#     else:
#         idx = bisect.bisect_left(dp, arr[i])
#         dp[idx] = arr[i]

# print(len(dp))