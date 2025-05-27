import sys
input = sys.stdin.readline

# def recur(x, y, n):
#     color_paper = paper[x][y]
#     for i in range(x, x+n):
#         for j in range(y, y+n):
#             if color_paper != paper[i][j]:
#                 recur(x,y,n//2)    # 1사분면
#                 recur(x,y+n//2, n//2)  # 2사분면
#                 recur(x+n//2, y, n//2)  # 3사분면
#                 recur(x+n//2, y+n//2, n//2)  # 4사분면
#                 return
#     if color_paper == 0:
#         result.append(0)
#     else:
#         result.append(1)
            

# n = int(input())
# paper = [list(map(int, input().split())) for _ in range(n)]
# result = []

# recur(0,0,n)

# print(result.count(0))
# print(result.count(1))


# ================================================
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white, bule = 0, 0

def recur(x,y,n):
    global white, bule

    color_paper = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color_paper != paper[i][j]:
                recur(x,y,n//2)
                recur(x+n//2,y,n//2)
                recur(x,y+n//2,n//2)
                recur(x+n//2,y+n//2,n//2)
                return
    if color_paper == 0:
        white += 1
    else:
        bule += 1

recur(0,0,n)

print(white, bule, sep='\n')
