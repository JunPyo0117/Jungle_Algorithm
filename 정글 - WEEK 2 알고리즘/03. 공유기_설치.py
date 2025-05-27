import sys
input = sys.stdin.readline

def can_place(mid):
    count = 1  # 첫번째 집에는 항상 공유기를 설치
    last = x[0]  # 마지막으로 공유기 설치한 위치 초기값(첫집)

    for i in range(1, len(x)):
        # 현재 집과 마지막으로 공유기를 설치한 집 사이의 거리가 mid 이상이어야 함
        # mid는 우리가 찾고자 하는 "가장 인접한 두 공유기 사이의 거리"의 최대값
        # 따라서 두 공유기 사이의 거리는 최소 mid 이상이어야 함
        if x[i] - last >= mid:
            count += 1
            last = x[i]
    
    return count >= c  # c개 이상 설치 가능?

def search():
    l, r = 1, max(x)-min(x)  # 가능한 최소 거리(1)부터 최대 거리(집들 사이의 최대 거리)까지 탐색
    answer = 0
    while l <= r:
        mid = (l+r) //2  # 인접한 두 공유기 사이의 최대 거리(구해야하는 값)
        if can_place(mid):  # mid 거리로 c개 이상 설치 가능하면
            answer = mid    # 정답 갱신
            l = mid +1     # 더 큰 거리 시도
        else:
            r = mid -1     # 더 작은 거리 시도
    return answer

n, c = map(int, input().split())
x = list(int(input()) for _ in range(n))
x.sort()

print(search())

# ===================================================
import sys
input = sys.stdin.readline

def search(target, l, r):
    while l <= r:
        mid = (l + r) // 2  # 공유기 간 최소 거리 후보 (중간값)

        current = x[0]      # 첫 번째 집에는 무조건 공유기 설치 (가장 왼쪽 집)
        cnt = 1             # 공유기 설치 개수 (첫 집에 설치했으므로 1개부터 시작)

        for i in range(1, len(x)):
            # 현재 설치한 공유기에서 mid 거리 이상 떨어져 있으면 설치 가능
            if x[i] >= current + mid:
                cnt += 1            # 공유기 설치
                current = x[i]      # 현재 위치 업데이트 (가장 마지막으로 설치한 곳)

        if cnt >= c:
            # 설치한 공유기 수가 충분함 → 최소 거리를 더 늘려도 될지 시도
            global answer           # 전역 변수에 저장
            answer = mid            # 현재 mid 값을 정답 후보로 저장
            l = mid + 1             # 최소 거리 범위를 더 키워본다 (왼쪽 경계 이동)
        else:
            # 공유기 수가 부족함 → 최소 거리를 줄여야 함
            r = mid - 1             # 오른쪽 경계를 줄인다

n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()

l, r = 1, x[-1] - x[0]  # 가능한 공유기 간 최소 거리 범위
answer = 0

search(x, l, r)
print(answer)