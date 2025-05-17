import sys

input = sys.stdin.readline

a = int(input())

for _ in range(a):
    b = input()
    b = b.replace('X', ' ')
    b = list(b.split())
    score = 0

    # print(b)

    for i in b:
        score += len(i)*(len(i)+1)//2

    print(score)

# ==================================
# 
import sys

input = sys.stdin.readline

a = int(input())

for _ in range(a):
    t = list(input())
    cnt, sum_score = 0, 0  
    for i in t:
        if i == "O":
            cnt += 1
            sum_score += cnt
        else:
            cnt = 0
    print(sum_score)    
    
    
    




