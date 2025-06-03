import sys
import heapq

# 입력 받기
n = int(sys.stdin.readline())
people = []

for _ in range(n):
    h, o = map(int, sys.stdin.readline().split())
    # 항상 작은 값이 왼쪽, 큰 값이 오른쪽에 오도록 정리
    if h > o:
        h, o = o, h
    people.append((h, o))

# 철로의 길이
d = int(sys.stdin.readline())

# 집과 사무실 거리가 철로 길이보다 긴 사람들 제외
# (이런 사람들은 절대 철로의 혜택을 받을 수 없음)
valid_people = []
for h, o in people:
    if o - h <= d:  # 거리가 철로 길이 이하인 경우만
        valid_people.append((h, o))

# 오른쪽 끝점(사무실) 기준으로 정렬
# 이렇게 하면 철로를 오른쪽으로 한 칸씩 이동시키는 효과
valid_people.sort(key=lambda x: x[1])

# 우선순위 큐(최소 힙) - 집 위치들을 저장
min_heap = []
max_count = 0

for home, office in valid_people:
    # 현재 사람의 사무실을 철로의 오른쪽 끝으로 설정
    right_end = office
    left_end = right_end - d  # 철로의 왼쪽 끝
    
    # 철로 범위에서 벗어난 사람들 제거
    # 힙의 최솟값이 철로 왼쪽 끝보다 작으면 제거
    while min_heap and min_heap[0] < left_end:
        heapq.heappop(min_heap)
    
    # 현재 사람의 집 위치를 힙에 추가
    heapq.heappush(min_heap, home)
    
    # 현재 철로에 포함되는 사람 수의 최댓값 갱신
    max_count = max(max_count, len(min_heap))

print(max_count)
