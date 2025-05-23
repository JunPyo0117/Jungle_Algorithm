# 더하기 사이클 1
n = input()

if int(n) < 10:
    n = '0' + n # n -> 0n

num = n
cnt = 0

while True:
    if num == n and cnt > 0:
        break
        
    sum_n = int(num[0]) + int(num[1])

    if sum_n < 10:
        sum_n = '0' + str(sum_n)
    else:
        sum_n = str(sum_n)
        
    num = num[1] + sum_n[-1]
    cnt += 1

print(cnt)







