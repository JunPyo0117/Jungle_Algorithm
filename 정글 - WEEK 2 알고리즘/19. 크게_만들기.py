# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# num = input()
# cnt = 0
# stack = []
# # print(type(num[0]))

# for i in range(n):
#     if not stack or stack[-1] > int(num[i]):
#         stack.append(int(num[i]))
#         # print(stack)
#     else:
#         if stack[-1] < int(num[i]):
#             cnt += 1
#             stack.pop()
#             stack.append(int(num[i]))
#             print(stack)
#             if cnt == k:
#                 stack.append(int(num[i]))


# print(*stack, sep='')
# =============================================================
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = input().strip()
cnt = 0
stack = []

for i in range(n):
    # 스택이 비어있지 않고, 현재 숫자가 스택의 마지막 숫자보다 크고, 아직 k개를 제거하지 않았다면
    while stack and stack[-1] < int(num[i]) and cnt < k:
        stack.pop()
        cnt += 1
    stack.append(int(num[i]))

# 아직 k개를 제거하지 못했다면 뒤에서부터 제거, 같은 숫자로만 이루어질 때 대비
while cnt < k:
    stack.pop()
    cnt += 1

print(*stack, sep='')
