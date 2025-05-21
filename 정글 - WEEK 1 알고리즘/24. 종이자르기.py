import sys

input = sys.stdin.readline

w, h = map(int, input().split())
cnt = int(input())

# 가로/세로 자르기 위치 저장
w_cuts = [0, w]  # 시작점과 끝점
h_cuts = [0, h]  # 시작점과 끝점

# 자르기 입력 받기
for _ in range(cnt):
    d, point = map(int, input().split())
    # 가로
    if d == 0:
        h_cuts.append(point)
    # 세로
    else:
        w_cuts.append(point)
print(w_cuts, h_cuts)
# 정렬
w_cuts.sort()
h_cuts.sort()


# 가장 큰 영역 찾기
max_area = 0
for i in range(len(w_cuts)-1):
    for j in range(len(h_cuts)-1):
        area = (w_cuts[i+1] - w_cuts[i]) * (h_cuts[j+1] - h_cuts[j])
        max_area = max(max_area, area)

print(max_area)


