import sys
input = sys.stdin.readline

def get_total_wood(height, trees):
    total = 0
    for tree in trees:
        if tree > height:
            total += tree - height
    return total

def binary_search(target, trees):
    left = 0
    right = max(trees) - 1
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        total = get_total_wood(mid, trees)
        
        if total >= target:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return result

n, m = map(int, input().split())
trees = list(map(int, input().split()))

print(binary_search(m, trees))

#====================================
N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) #이분탐색 검색 범위 설정

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2
    
    total = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid:
            total += i - mid
    
    #벌목 높이를 이분탐색
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)









