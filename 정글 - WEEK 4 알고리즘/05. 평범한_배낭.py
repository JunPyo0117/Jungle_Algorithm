# 평범한 배낭 문제 (Knapsack Problem) - 동적 계획법으로 해결
import sys
input = sys.stdin.readline

def dynamic(goods):
    # dp[i][j]: i번째 물건까지 고려했을 때, 무게 제한 j 이하에서 얻을 수 있는 최대 가치
    dp = [[0] * (k+1) for _ in range(n+1)]

    # 모든 물건에 대해 반복
    for i in range(1, n+1):
        # 모든 무게 제한에 대해 반복
        for j in range(1, k+1):
            w = goods[i-1][0]  # 현재 물건의 무게
            v = goods[i-1][1]  # 현재 물건의 가치

            # 현재 물건의 무게가 배낭 용량보다 크면
            if j < w:
                # 현재 물건을 넣을 수 없으므로 이전 상태 그대로 유지
                dp[i][j] = dp[i-1][j]
            else:
                # 현재 물건을 넣지 않는 경우와 넣는 경우 중 최대값 선택
                # dp[i-1][j]: 현재 물건을 넣지 않는 경우
                # dp[i-1][j-w] + v: 현재 물건을 넣는 경우 (남은 용량에서의 최대값 + 현재 물건의 가치)
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
    
    # 모든 물건을 고려했을 때 최대 무게 제한에서의 최대 가치 출력
    print(dp[n][k])
        
# 물건 개수, 최대 무게
n, k = map(int, input().split())
#무게, 가치
goods = [list(map(int, input().split())) for _ in range(n)]

dynamic(goods) 