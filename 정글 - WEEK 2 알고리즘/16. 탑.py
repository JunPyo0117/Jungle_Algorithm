import sys
input = sys.stdin.readline

n = int(input())
stack = []   # 타워 인덱스 저장 
towers = list(map(int, input().split())) # 타워의 높이와 순서 
# answer = {v: i for v, i in enumerate(towers, 1)}

# for i in range(n):
#     if stack[-1] < towers[i]:
#         stack.pop()
#     stack.append(towers[i])

        
# print(answer)
# print(stack)

# for i in towers:
#     if i < stack[0]:
#         print(0, end=' ')

# ====================================
result = [0] * n  # 결과를 저장할 리스트 (초기값은 전부 0)

for i in range(n):
    # 현재 타워보다 낮은 타워는 레이저를 받을 수 없으므로 제거
    while stack and towers[stack[-1]] < towers[i]:
        stack.pop()
    
    if stack:
        # 스택이 비어 있지 않으면 → 현재 타워의 레이저가 닿는 타워가 있음
        # stack[-1]은 레이저를 수신하는 가장 가까운 왼쪽 타워의 인덱스
        result[i] = stack[-1] + 1  # +1은 문제에서 인덱스가 1부터 시작하기 때문
    else:
        # 스택이 비어 있으면 → 왼쪽에 자신보다 높은 타워가 없음 → 0 (기본값 유지)
        pass

    # 현재 타워의 인덱스를 스택에 추가
    # 이후 들어올 타워들의 레이저 수신 여부를 판단할 기준이 됨
    stack.append(i)

# 결과 출력 (리스트를 언팩하여 공백 구분으로 출력)
print(*result)

# ====================================
import sys
input = sys.stdin.readline

n = int(input())    # 타워의 개수
towers = list(map(int, input().split()))  # 각 타워의 높이 (왼쪽부터 오른쪽 순서)

stack = [0]  # 처음 비교할 기준 높이 (0부터 시작하면 예외 처리 쉽게 가능)

# 각 타워의 높이를 key, 위치(1-based index)를 value로 저장
tower_idx_finder = {v: i for i, v in enumerate(towers, 1)}

for tower in towers:
    while stack[-1] <= tower:
        stack.pop()  # 현재 타워보다 낮은 타워는 신호를 받을 수 없으므로 제거

        if not stack:
            # 더 이상 왼쪽에 높은 타워가 없으면 0 출력
            print(0, end=" ")
            stack.append(tower)  # 현재 타워를 기준으로 다시 스택 구성
            break
    else:
        # 왼쪽에서 신호를 받을 수 있는 첫 번째 높은 타워의 인덱스를 출력
        print(tower_idx_finder[stack[-1]], end=" ")
        stack.append(tower)  # 현재 타워도 스택에 추가 (뒤에 오는 타워를 위해)