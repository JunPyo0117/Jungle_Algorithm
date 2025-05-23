import sys
input = sys.stdin.readline

def recur(n, paper):
    if n == 0:
        return 0
    
    recur(n//2, paper)

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

print(paper)