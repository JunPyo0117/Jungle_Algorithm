import sys

input = sys.stdin.readline

# 점의 개수 입력
n = int(input())

# 모든 점들을 저장할 리스트
points = []

# 점들 입력받기
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    
# x좌표 기준으로 정렬 (분할정복을 위한 전처리)
points.sort()

def compute_min_dist(start, end):
    """
    작은 범위에서 모든 쌍을 비교하는 무차별 대입법
    점이 적을 때 사용 (기저 조건)
    """
    min_dist = int(1e10)  # 충분히 큰 값으로 초기화
    
    for i in range(start, end-1):
        for j in range(i+1, end):
            # 두 점 사이의 거리의 제곱 계산
            dist = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
            min_dist = min(min_dist, dist)
    return min_dist

def find_min_dist(start, end):
    """
    분할정복으로 가장 가까운 두 점의 거리를 찾는 메인 함수
    start: 시작 인덱스, end: 끝 인덱스
    """
    size = end - start
    
    # 기저 조건: 점이 3개 미만이면 무차별 대입으로 해결
    if size < 3:
        return compute_min_dist(start, end)
    
    # 중간점을 기준으로 분할
    mid = (start + end) // 2
    
    # 분할: 왼쪽 영역과 오른쪽 영역에서 각각 최솟값 구하기
    left = find_min_dist(start, mid)    # 왼쪽 영역의 최단거리
    right = find_min_dist(mid, end)     # 오른쪽 영역의 최단거리
    
    # 정복: 왼쪽과 오른쪽 중 더 작은 거리
    min_dist = min(left, right)
    
    # 합치기: 중간 경계선을 넘나드는 점들 중에서 더 가까운 쌍이 있는지 확인
    check_point = []
    divide_x = points[mid][0]  # 분할선의 x좌표
    
    # 분할선에서 min_dist 거리 내에 있는 점들만 후보로 선택
    # 이 범위 밖의 점들은 절대 답이 될 수 없음
    for i in range(start, end):
        if (points[i][0] - divide_x)**2 <= min_dist:
            check_point.append(points[i])
    
    # 후보 점들을 y좌표 기준으로 정렬
    # y좌표 순으로 비교해야 효율적
    check_point.sort(key=lambda x:x[1])
    
    # 중간 영역에서 가장 가까운 두 점 찾기
    for i in range(len(check_point)):
        now = check_point[i]  # 현재 점
        
        # 현재 점보다 y좌표가 큰 점들과 비교
        for j in range(i+1, len(check_point)):
            compare = check_point[j]  # 비교할 점
            
            # y좌표 차이가 이미 min_dist보다 크면 더 이상 확인할 필요 없음
            # (y좌표로 정렬되어 있으므로 그 이후 점들은 더 멀어짐)
            if (compare[1] - now[1])**2 >= min_dist:
                break
            
            # 실제 거리 계산하고 최솟값 업데이트
            dist = (now[0] - compare[0])**2 + (now[1] - compare[1])**2
            min_dist = min(min_dist, dist)
    
    return min_dist 

# 전체 범위에서 가장 가까운 두 점의 거리의 제곱 출력
print(find_min_dist(0, n))