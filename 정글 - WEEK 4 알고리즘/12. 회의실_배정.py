import sys
input = sys.stdin.readline

n = int(input())

meeting_list = [list(map(int, input().split())) for _ in range(n)]
meeting_list.sort(key=lambda x: (x[1], x[0]))
# meeting_list.sort(key=lambda x: x[0]) # 두 번째 요소만 정렬되서 안됨
# print(meeting_list)

cnt = 0
end_time = 0

for start, end in meeting_list:
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)
