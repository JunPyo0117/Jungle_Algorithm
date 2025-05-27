import heapq  # 파이썬의 heapq 모듈 사용 (기본적으로 최소 힙 구조)
import sys     # 빠른 입력을 위해 sys 모듈 사용

n = int(sys.stdin.readline())  # 전체 숫자의 개수 입력

# 왼쪽 힙 (최대 힙처럼 사용할 예정): 중앙값 이하의 값들을 저장
# 파이썬은 최대 힙이 없기 때문에 음수로 저장해서 최대 힙처럼 사용
maxHeap = []
# 오른쪽 힙 (최소 힙): 중앙값보다 큰 값들을 저장
minHeap = []

for i in range(n):
    num = int(sys.stdin.readline())  # 새로운 수 입력

    # 양쪽 힙의 길이가 같을 경우, 새로운 수는 무조건 maxHeap에 넣는다
    # 중앙값이 항상 maxHeap에 있게 유지하기 위해서 (중앙값은 작은 쪽이 많거나 같을 때 작동)
    if len(maxHeap) == len(minHeap):
        heapq.heappush(maxHeap, -num)  # 최대 힙처럼 사용하기 위해 음수로 저장
    else:
        # 두 힙의 길이가 다르면 (left가 더 많으면), right에 삽입
        heapq.heappush(minHeap, num)  # 최소 힙은 양수 그대로 저장

    # 두 힙의 루트 값을 비교해서 정렬 조건이 어긋났는지 확인
    # 오른쪽 힙의 최솟값이 왼쪽 힙의 최댓값보다 작으면 (잘못된 상태) → 교환 필요
    if minHeap and minHeap[0] < -maxHeap[0]:
        minValue = heapq.heappop(maxHeap)   # maxHeap의 루트 (최댓값, 음수로 저장됨)
        maxValue = heapq.heappop(minHeap) # minHeap의 루트 (최솟값)

        # 교환하여 힙 상태를 정리함
        heapq.heappush(maxHeap, -maxValue)  # 오른쪽의 값을 왼쪽으로 (음수로 저장)
        heapq.heappush(minHeap, -minValue)  # 왼쪽의 값을 오른쪽으로 (음수였으므로 다시 양수로)

    # 항상 maxHeap의 루트가 중앙값이 되도록 유지됨
    # 이유: maxHeap이 minHeap보다 크거나 같도록 유지했기 때문
    print(-maxHeap[0])  # maxHeap은 음수로 저장되어 있으므로 다시 양수로 출력






