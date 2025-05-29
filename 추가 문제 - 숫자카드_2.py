import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

# print(n_list)

dic = {}

for i in n_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for chk in m_list:
    if chk in dic:
        print(dic[chk], end=" ")
    else:
        print(0, end=" ")

# print(dic)
# ========================
import sys
import bisect
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

# 이분탐색을 위해 정렬
n_list.sort()

for target in m_list:
    # bisect_left: target이 처음 나타나는 위치 (lower_bound와 동일)
    # bisect_right: target보다 큰 값이 처음 나타나는 위치 (upper_bound와 동일)
    left = bisect.bisect_left(n_list, target)
    right = bisect.bisect_right(n_list, target)
    count = right - left
    print(count, end=" ") 