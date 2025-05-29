import sys
input = sys.stdin.readline

n = int(input())

circle_info = [list(map(int, input().split())) for _ in range(n)]  # x = 원의 중심, r = 반지름

# circle_line = []

# for x, r in circle_info:
#     circle_line.append([x-r, 1]) # 왼쪽 원 시작
#     circle_line.append([x+r, 2]) # 오른쪽 원 시작
# circle_line.sort() # 왼쪽 점부터 오른쪽 점까지 정렬

# stack = []
# cnt = 0
# for i in range(len(circle_line)):
#     stack.append(circle_line[i])
#     if len(stack) >= 2 and stack[-2][1] == 1 and stack[-1][1] == 2: # 스택의 마지막 두 원소 비교
#         stack.pop()  # 끝점 제거
#         stack.pop()  # 시작점 제거
#         cnt += 1
        
# print(stack)
# print(cnt)
# =========================================================================================

points = []
for x, r in circle_info:
    points.append(("L", x-r))
    points.append(("R", x+r))

points.sort(key=lambda p: (-p[1], p[0]), reverse=True)

stack = []
area = 1
for curr in points:
    if curr[0] == "L":
        stack.append(curr)
        continue
    
    cum_width = 0
    while stack:
        prev = stack.pop()
        if prev[0] == "C":
            cum_width += prev[1]        
        elif prev[0] == "L":
            width = curr[1] - prev[1]
            if width == cum_width:
                area += 2
            else:
                area += 1
            stack.append(("C", width)) 
            break
    
print(area)

