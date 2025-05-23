import sys
input = sys.stdin.readline

def search(target, arr):
    l, r = 0, len(arr)-1

    while l <= r:
        mid = (l+r)//2
        
        if arr[mid] == target:
            return 1
        elif target < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return 0

# 첫 번째 배열의 크기 입력
n = int(input())
# 첫 번째 배열 입력 및 정렬
a = list(map(int, input().split()))
a.sort()  # 이진 탐색을 위해 정렬 필수

# 두 번째 배열의 크기 입력
m = int(input())
# 두 번째 배열 입력
b = list(map(int, input().split()))

# 두 번째 배열의 각 원소가 첫 번째 배열에 있는지 확인
for i in b:
    # 있으면 1, 없으면 0 출력
    print(search(i, a))