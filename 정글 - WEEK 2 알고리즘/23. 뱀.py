import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
apple = int(input())
apple_coord = [tuple(map(int, input().split())) for _ in range(apple)]
l = int(input())
direction = [input().strip().split() for _ in range(l)]

current = deque([(1,1)])

dir = 0  # 0 오른쪽 방향, 1 아래, 2 왼쪽, 3 위
dx = [0, 1, 0, -1]  # 오른쪽, 아래, 왼쪽, 위 
dy = [1, 0, -1, 0]
# direct = [(0,1), (1,0), (0,-1), (-1,0)] # 오른쪽, 아래, 왼쪽, 위 

time = 0
direction_index = 0

while True:
    time += 1

    head_x, head_y = current[-1]

    # 새로운 머리 위치 계산
    new_x = head_x + dx[dir]
    new_y = head_y + dy[dir]

    # 2. 충돌 체크 (범위를 벗어났을 때, 내 몸통에 닿았을 때)
    if new_x < 1 or new_x > n or new_y < 1 or new_y > n: # n 범위를 벗어나거나, 음수일 떄
        break
    if (new_x, new_y) in current:
        break

    # 3. 새 머리 추가
    current.append((new_x, new_y))

    # 4. 사과 체크
    if (new_x, new_y) in apple_coord:
        # 사과 먹음 → 꼬리 안 자름
        apple_coord.remove((new_x, new_y))
    else:
        # 사과 안 먹음 → 꼬리 자름
        current.popleft()
    # 5. 방향 전환 체크
    if direction_index < l and time == int(direction[direction_index][0]):
        if direction[direction_index][1] == 'D':
            dir = (dir + 1) % 4  # 오른쪽 회전
        else:  # 'L'
            dir = (dir - 1) % 4  # 왼쪽 회전
        direction_index += 1

print(time)
    
    
# for i, v in direction:
#     for j in range(int(i)):
#         head_x, head_y = current[-1]  # 머리는 항상 deque의 마지막
#         nx = head_x + dx[dir]
#         ny = head_y + dy[dir]
#         current.append((nx, ny))  # 머리 이동
#         if (nx, ny) in apple_coord:
#             continue
#         else:
#             current.popleft()
#     if v == 'D':
#         dir = (dir + 1) % 4
#     else:
#         dir = (dir - 1) % 4
    
            

