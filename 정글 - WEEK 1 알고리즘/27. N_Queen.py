import sys
input = sys.stdin.readline

n = int(input())

cols = [False] * n              # 열 정보
diag_a = [False] * (2 * n - 1)  # / 대각선 정보
diag_b = [False] * (2 * n - 1)  # \ 대각선 정보

def place_row(i):
    if i >= n:
        return 1

    count = 0
    for j in range(n):
        if (not cols[j] and not diag_a[i + j] and not diag_b[i - j + n - 1]):
            cols[j] = diag_a[i + j] = diag_b[i - j + n - 1] = True
            count += place_row(i + 1)
            cols[j] = diag_a[i + j] = diag_b[i - j + n - 1] = False
    return count

print(place_row(0))