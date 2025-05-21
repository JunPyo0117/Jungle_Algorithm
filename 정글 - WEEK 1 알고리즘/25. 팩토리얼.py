import sys

input = sys.stdin.readline

def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1

print(factorial(int(input())))

# ===================================
# 반복문 while로 풀기
import sys

input = sys.stdin.readline

n = int(input())

multi_num = 1  # 초기값을 1로 설정

while n > 0:
    multi_num *= n 
    n = n - 1 

print(multi_num)

