import sys
input = sys.stdin.readline

my_string = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(my_string)):

    if my_string[i] == "(":
        stack.append(my_string[i])
        tmp *= 2

    elif my_string[i] == "[":
        stack.append(my_string[i])
        tmp *= 3

    elif my_string[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if my_string[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if my_string[i-1] == "[":
            answer += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)