import sys
from queue import PriorityQueue
input = sys.stdin.readline

#=============================================
# n = int(input())
# queue = []
# # print(len(queue))
# for _ in range(n):
#     x = int(input())

#     if x == 0 and len(queue) == 0:
#         print(0)
#     elif x == 0:
#         print(queue.pop())
#     elif x > 0:
#         queue.append(x)
#         queue.sort()
    
# ====================================
n = int(input())
pq = PriorityQueue()

for _ in range(n):
    x = int(input())
    if x == 0 and pq.empty():
        print(0)
    elif x == 0:
        print(-pq.get())
    elif x > 0:
        pq.put(-x)
    
