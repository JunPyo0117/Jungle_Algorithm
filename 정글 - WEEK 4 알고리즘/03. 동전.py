import sys
input = sys.stdin.readline

def dynamic(coin, amount):
    # dp[i] = i원을 만들 수 있는 경우의 수를 저장하는 배열
    dp = [0] * (amount+1)
    # 0원을 만드는 경우의 수는 1 (아무 동전도 사용하지 않는 경우)
    dp[0] = 1
    
    # 각 동전 종류별로 처리 (중복 방지를 위해 동전 순서대로)
    for c in coin:
        # 현재 동전(c)을 사용해서 c원부터 amount원까지 만들 수 있는 경우의 수 갱신
        for i in range(c, amount+1):
            # i원을 만드는 경우의 수 = 기존 경우의 수 + (i-c)원을 만드는 경우의 수
            # (현재 동전 c를 추가로 사용하는 경우)
            dp[i] += dp[i-c]
    
    # 목표 금액(amount)을 만들 수 있는 총 경우의 수 반환
    return dp[amount]

t = int(input())

for _ in range(t):
    n = int(input())  # 동전 종류의 수
    coin = list(map(int, input().split()))  # 동전들의 값
    amount = int(input())  # 만들어야 할 금액
    print(dynamic(coin, amount))
    

