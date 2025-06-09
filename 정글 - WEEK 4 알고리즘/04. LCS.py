import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# # LCS 출력 
# def get_text(r, c):
#     if r == 0 or c == 0:
#         return
#     if a[r-1] == b[c-1]:  # 문자열이 같으면 
#         path.append(a[r-1])  # 배열에 저장
#         get_text(r-1, c-1) # 왼쪽 대각선으로 이동 재귀
#     else:
#         if dp[r-1][c] > dp[r][c-1]: # 다르면 왼쪽과 위쪽중 큰 값을 비교
#             get_text(r-1,c)
#         else:
#             get_text(r, c-1)

a = list(input().rstrip())
b = list(input().rstrip())

dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
path = []

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(a)][len(b)])

# get_text(len(a),len(b))
# path.reverse()
# print(''.join(path))