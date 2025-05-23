import sys
input = sys.stdin.readline

def binarySearch(target, arr):
    # 이진 탐색의 범위를 정의 (왼쪽 끝, 오른쪽 끝)
    l, r = 0, len(a)-1
    
    # l이 r보다 커지면 탐색 종료
    while l <= r:
        # 중간값 계산 (정수 나눗셈 사용)
        mid = (l+r)//2
        
        # 찾는 값과 중간값이 같으면 True 반환
        if a[mid] == target:
            return 1
        # 중간값이 찾는 값보다 작으면 오른쪽 범위 탐색
        elif a[mid] < target:
            l = mid + 1
        # 중간값이 찾는 값보다 크면 왼쪽 범위 탐색
        elif target < a[mid]:
            r = mid - 1

    # 탐색이 끝났는데 값을 찾지 못하면 False 반환
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
    print(binarySearch(i, a))
