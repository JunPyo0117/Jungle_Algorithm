import sys

t = int(sys.stdin.readline())


for _ in range(t):
    vps = sys.stdin.readline()

    stack = 0
    for i in vps:
        if i == "(":
            stack += 1
            # print(stack)
        elif i == ")":
            stack -= 1
            if stack < 0:
                break
            # print(stack)
    
    if stack == 0:
        print("YES")
    else:
        print("NO")