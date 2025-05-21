import sys

input = sys.stdin.readline

def hanoi(n, x, y):
    if n > 1:
        hanoi(n-1, x, 6-x-y)
    print(x, y)
    if n > 1:
        hanoi(n-1, 6-x-y, y)

n = int(input())
print(2**n-1)  # 총 이동 횟수는 2^n - 1

if n <= 20:  # 20 이하일 때만 이동 과정 출력
    hanoi(n, 1, 3)
