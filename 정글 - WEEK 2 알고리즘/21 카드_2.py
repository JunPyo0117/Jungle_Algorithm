import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

num_list = deque(range(1,n+1))
# num_list.rotate()
# print(num_list)

for i in range(n):
    while len(num_list) > 1:
        num_list.popleft()
        num_list.rotate(-1)
        # print(num_list)

print(*num_list)

# ======================================
import sys
from collections import deque

n = int(sys.stdin.readline())
card = deque(range(1, n+1))

while True:
    if len(card) == 1:
        print(card[0])
        break

    card.popleft()
    card.append(card.popleft())