# 1,2,3 더하기  2
# 1,2,3 중복 가능, 더해서 n이 되는 수 조합 

def recur(n):
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return recur(n-1) + recur(n-2) + recur(n-3)

t = int(input())

for i in range(t):
    print(recur(int(input())))


# 재귀적 방식으로 작성해야함


