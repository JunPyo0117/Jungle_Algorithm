# import sys
# import heapq
# input = sys.stdin.readline

# n = int(input())
# pq = [int(input()) for _ in range(n)]
# pq.h()

# result = []

# first_sum = pq[0] + pq[1]
# result.append(first_sum)

# for i in range(2,n):
#     result.append(first_sum + pq[i])
#     print(result)

# print(sum(result))

#===============================
import sys
import heapq

input = sys.stdin.readline

n = int(input())
pq = [int(input()) for _ in range(n)]

heapq.heapify(pq)  

total_cost = 0

while len(pq) > 1:
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)
    cost = a + b
    total_cost += cost
    heapq.heappush(pq, cost)

print(total_cost)