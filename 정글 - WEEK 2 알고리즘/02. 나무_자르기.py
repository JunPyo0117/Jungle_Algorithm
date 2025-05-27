import sys
input = sys.stdin.readline

# def get_total_wood(height, trees):
#     total = 0
#     for tree in trees:
#         if tree > height:
#             total += tree - height
#     return total

# def binary_search(target, trees):
#     left = 0
#     right = max(trees) - 1
#     result = 0
    
#     while left <= right:
#         mid = (left + right) // 2
#         total = get_total_wood(mid, trees)
        
#         if total >= target:
#             result = mid
#             left = mid + 1
#         else:
#             right = mid - 1
            
#     return result

# n, m = map(int, input().split())
# trees = list(map(int, input().split()))

# print(binary_search(m, trees))

#====================================
# n: 나무의 수, m: 필요한 나무 길이
n, m = map(int, input().split())
tree = list(map(int, input().split()))

# 이분 탐색의 탐색 범위: 최소 1부터 가장 큰 나무의 높이까지
start, end = 1, max(tree)

# 적절한 절단 높이를 찾기 위한 이분 탐색
while start <= end:
    mid = (start + end) // 2  # 현재 설정할 절단기 높이 (중간값)

    total = 0  # 잘린 나무 총 길이 계산
    for i in tree:
        if i >= mid:
            total += i - mid  # mid보다 큰 나무만 잘림

    # 필요한 나무 길이 m보다 많이 잘렸으면 절단 높이를 더 높여도 됨
    if total >= m:
        start = mid + 1
    # 너무 적게 잘렸으면 절단 높이를 낮춰야 함
    else:
        end = mid - 1

# 최종적으로 end는 나무를 m만큼 가져갈 수 있는 가장 높은 절단기 높이
print(end)









