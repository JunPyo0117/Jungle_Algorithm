# 프린터 큐
# 현재 Queue의 가장 앞에 있는 문서의 '중요도'를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
# 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄
# 3
# 1 0
# 5
# 4 2
# 1 2 3 4
# 6 0
# 1 1 9 1 1 1 왜 5번쨰인지 모르겠음 
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    n, m = map(int, input().split())
    # (중요도, 원래 위치) 형태로 저장
    queue = deque([(val, idx) for idx, val in enumerate(map(int, input().split()))])
    count = 0
    
    while queue:
        # max(queue, key=lambda x: x[0])는 (중요도, 원래 위치) 튜플을 반환
        # [0]을 붙여서 중요도 값만 가져옴
        # 예: queue = [(5, 0), (2, 1), (9, 2)]일 때
        # max()는 (9, 2)를 반환하고, [0]으로 9만 가져옴
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            # 원하는 문서가 인쇄되었는지 확인
            if queue[0][1] == m:
                print(count)
                break
            queue.popleft()
        else:
            # 중요도가 낮으면 뒤로 보내기
            # queue.append(queue.popleft())
            queue.rotate(-1)
