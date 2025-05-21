# 시간 초과
import sys

input = sys.stdin.readline

# 0과 1은 소수가 아니므로 False, 나머지 9,999개를 True로 초기화 (소수 판별용)
is_prime = [False, False] + [True] * 9998
prime = []

# 에라토스테네스의 체 알고리즘으로 소수 목록을 미리 구함
for i in range(2, int(10000 ** 0.5) + 1):  # 2부터 √1,000,000까지 반복
    if is_prime[i]:  # i가 소수이면
        for j in range(i*i, 10000, i):  # i의 배수들은 소수가 아니므로
            is_prime[j] = False  # 해당 인덱스를 False로 마킹

for j in range(len(is_prime)):
    if is_prime[j]:
        prime.append(j)

# print(prime)

t = int(input())

for _ in range(t):
    n = int(input())
    start = 0
    end = len(prime) - 1
    min_diff = float('inf')
    answer = []
    
    # 모든 소수 쌍을 검사
    for i in range(len(prime)):
        for j in range(i, len(prime)):
            if prime[i] + prime[j] == n:
                diff = prime[j] - prime[i]
                if diff < min_diff:
                    min_diff = diff
                    answer = (prime[i], prime[j])
    
    print(answer[0], answer[1])
            
                
#=================================================================
# 쌍으로 
import sys

input = sys.stdin.readline

# 0과 1은 소수가 아니므로 False, 나머지 9,999개를 True로 초기화 (소수 판별용)
is_prime = [False, False] + [True] * 9998
prime = []

# 에라토스테네스의 체 알고리즘으로 소수 목록을 미리 구함
for i in range(2, int(10000 ** 0.5) + 1):  # 2부터 √1,000,000까지 반복
    if is_prime[i]:  # i가 소수이면
        for j in range(i*i, 10000, i):  # i의 배수들은 소수가 아니므로
            is_prime[j] = False  # 해당 인덱스를 False로 마킹

for j in range(len(is_prime)):
    if is_prime[j]:
        prime.append(j)

# print(prime)

t = int(input())

for _ in range(t):
    n = int(input())
    start = 0
    end = len(prime) - 1
    answer = []
    
    # 투 포인터 방식으로 두 소수의 합이 n이 되는 쌍을 찾음
    while start <= end:
        sum_val = prime[start] + prime[end]
        if sum_val == n:
            answer = (prime[start], prime[end])
            start += 1
            end -= 1
        elif sum_val < n:
            start += 1
        else:
            end -= 1
    
    print(answer[0], answer[1])

# =========================================================
import sys

input = sys.stdin.readline

def d(N):
    if N == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if N % i == 0:
            return False
    return True

N = int(input())

for _ in range(N):
    num = int(input())

    # 입력받은 짝수를 두 수로 나누기
    # 중앙에서 시작하여 차이가 가장 작은 소수 쌍을 찾기 위함
    a = num // 2  # 첫 번째 수는 입력값의 절반
    b = num // 2  # 두 번째 수도 입력값의 절반

    # num//2번 반복하면서 소수 쌍 찾기
    # 중앙에서 시작하여 양쪽으로 퍼져나가며 검사
    for _ in range(num//2):
        if d(N) and d(a):  # 두 수가 모두 소수인지 확인
            print(a, b)    # 소수 쌍을 찾으면 출력
            break
        else:
            a-=1  # 첫 번째 수 감소
            b+=1  # 두 번째 수 증가

# =========================================================
# 중앙부터 시작하는 방식
import sys

input = sys.stdin.readline

# 0과 1은 소수가 아니므로 False, 나머지 9,999개를 True로 초기화 (소수 판별용)
is_prime = [False, False] + [True] * 9998

# 에라토스테네스의 체 알고리즘으로 소수 목록을 미리 구함
for i in range(2, int(10000 ** 0.5) + 1):  # 2부터 √1,000,000까지 반복
    if is_prime[i]:  # i가 소수이면
        for j in range(i*i, 10000, i):  # i의 배수들은 소수가 아니므로
            is_prime[j] = False  # 해당 인덱스를 False로 마킹

t = int(input())

for _ in range(t):
    n = int(input())
    
    # 중앙값부터 시작
    # 중앙값에서 가장 가까운 소수 찾기
    left = n // 2
    right = n // 2
    
    # 중앙에서부터 양쪽으로 퍼져나가며 검사
    while right < n:
        # 두 수가 모두 소수인지 확인
        if is_prime[left] and is_prime[right]:
            print(left, right)
            break
        # 한쪽은 감소, 다른 쪽은 증가
        left -= 1
        right += 1

# ====================================
# 소수판별 비효율적임
def is_prime_number(n):
    # 1은 소수가 아님
    if n == 1:
        return False
    
    # 2부터 n까지 나누어 떨어지는지 확인
    for i in range(2, n + 1):
        # 자기 자신은 건너뛰기
        if i == n:
            continue
        # 나누어 떨어지면 소수가 아님
        if n % i == 0:
            return False
    
    # 나누어 떨어지는 수가 없으면 소수
    return True

#=====================================
def test():
    n = int(input())

    def check(n):
        if n == 1:
            return False
        else:
            for i in range(2,int(n**0.5)+1):
                if n % i ==0:
                    return False
            return True

    for i in range(n):
        num = int(input())
        mid_num = num // 2
        
        for j in range(mid_num,1,-1):
            if check(j) and check(num-j):
                print(j,num-j)
                break

test()
