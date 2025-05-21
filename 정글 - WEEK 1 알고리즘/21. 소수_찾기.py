import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int, input().split()))
#print(num_list)
cnt = 0

for i in num_list:
    if i < 2:
        continue
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        cnt +=1

print(cnt)
    
