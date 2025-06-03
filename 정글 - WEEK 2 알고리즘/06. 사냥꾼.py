import sys

# 입력: 사대 수(M), 동물 수(N), 사정거리(L)
M, N, L = map(int, sys.stdin.readline().split())
hunters = list(map(int, sys.stdin.readline().split()))  # 사대 위치들
hunters.sort()  # 이분탐색을 위해 정렬

result = 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())  # 동물 좌표 (a, b)
    
    # 이분탐색으로 사격 가능한 사대 찾기
    left, right = 0, M - 1
    while left <= right:
        mid = (left + right) // 2
        distance = abs(hunters[mid] - a) + b  # 맨하탄 거리 계산
        
        if distance <= L:  # 사정거리 내에 있으면
            result += 1    # 카운트하고 다음 동물로
            break
        elif hunters[mid] < a:  # 사대가 동물보다 왼쪽에 있으면
            left = mid + 1      # 오른쪽 탐색
        else:                   # 사대가 동물보다 오른쪽에 있으면
            right = mid - 1     # 왼쪽 탐색

print(result)
