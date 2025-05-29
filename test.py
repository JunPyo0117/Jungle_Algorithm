import sys
input = sys.stdin.readline


my_string = input().rstrip()
boom = input().rstrip()

# for _ in range(len(my_string)//2):
#     if not my_string:
#         print("FRULA")
#     my_string = my_string.replace(boom, '')

# print(my_string)

# mirkovC4nizCC44
# C4

stack = []
for s in my_string:
    stack.append(s)
    if len(stack) >= len(boom):
        chk = stack[len(stack)-len(boom):]

        if ''.join(chk) == boom:
            for _ in range(len(boom)):
                stack.pop()
    

if not stack:
    print("FRULA")
else:
    print(''.join(stack))


