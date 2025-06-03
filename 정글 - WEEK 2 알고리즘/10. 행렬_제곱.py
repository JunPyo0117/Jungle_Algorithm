import sys

input = sys.stdin.readline

def matrix_multiply(a, b):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k]*b[k][j]
                result[i][j] %= 1000
    return result

def matrix_square(matrix, b):
    if b == 1:
        return matrix
    tmp = matrix_square(matrix, b // 2)    # 여기 수정
    if b % 2 == 0:
        return matrix_multiply(tmp, tmp)
    else:
        return matrix_multiply(matrix_multiply(tmp, tmp), matrix)
    
n, b = map(int, input().strip().split())
num_list = [list(map(int, input().split())) for _ in range(n)]

result = matrix_square(num_list, b)  # 결과 저장

for i in range(n):
    print(*result[i])


