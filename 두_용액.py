import sys
import bisect
input = sys.stdin.readline

# 모든 조합을 사용했지만 메모리 초과
# n = int(input())
# x = list(map(int, input().split()))

# arr = {}

# for i in permutations(x, 2):
#     if abs(sum(i)) > 0:
#         arr[abs(sum(i))] = i
# a = arr[min(arr)]
# print(a[1], a[0])

# =======================================
n = int(input())
x = list(map(int, input().split()))
x.sort()

min_sum = float('inf')
ans = (0, 0)

for i in range(n-1):
    target = -x[i]
    j = bisect.bisect_left(x, target, i+1, n)

    # x[j] 체크
    if j < n and abs(x[i] + x[j]) < abs(min_sum):
        min_sum = x[i] + x[j]
        ans = (x[i], x[j])

    # x[j-1] 체크
    if j - 1 > i and abs(x[i] + x[j-1]) < abs(min_sum):
        min_sum = x[i] + x[j-1]
        ans = (x[i], x[j-1])

print(ans[0], ans[1])

        
        

