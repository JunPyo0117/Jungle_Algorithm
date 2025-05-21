import sys

input = sys.stdin.readline

n = int(input())
cnt = 0

# 한수 = 각 자리의 숫자가 등차수열인 수
# 한 자리 수와 두 자리 수는 모두 한 수
for i in range(1, n+1):
    su = []
    if i < 100:
        cnt += 1
    else:
        num_str = str(i)
        # N 1000보다 작기 떄문에 두 수의 차이 2개가 같아야함
        if (int(num_str[1]) - int(num_str[0])) == (int(num_str[2]) - int(num_str[1])):
            cnt += 1

print(cnt)