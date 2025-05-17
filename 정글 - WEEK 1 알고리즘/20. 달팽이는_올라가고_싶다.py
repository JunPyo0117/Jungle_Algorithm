import sys

input = sys.stdin.readline

a, b, v = map(int, input().split())

# 올라가는 날 = x
# 아침에 올라가는 횟수 = x
# 밤에 떨어지는 횟수 = x-1
# v = ax - b(x-1)
# x = (v-b) / (a-b)

x = (v-b) / (a-b)

# 정수면 출력 
# else 0.xx 더 걸림 그러므로 하루 더 추가
if x == int(x):
    print(int(x))
else:
    print(int(x+1))