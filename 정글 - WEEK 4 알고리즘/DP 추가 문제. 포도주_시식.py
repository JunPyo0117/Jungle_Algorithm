import sys
input = sys.stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(wines))
else:
    # 6 10 13 9 8 1
    # i번째 와인까지 고려했을 때 얻을 수 있는 최댓값 
    dp = [0] * (n+1)
    dp[1] = wines[0] # 1
    dp[2] = wines[0] + wines[1] # 1,2
    # dp[3] = max(dp[1] + wines[2], dp[2], wines[1] + wines[2]) # 1,2 1,3 2,3

    for i in range(3, n+1):
        # 1,2 1,3 2,3
        # i번째 안 마심
        # i번째만 마심 (i-1번째 건너뜀)
        # i-1, i번째 둘 다 마심
        dp[i] = max(dp[i-1], dp[i-2] + wines[i-1], dp[i-3] + wines[i-1] + wines[i-2])
    
    print(dp[n])