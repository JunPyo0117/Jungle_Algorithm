import sys
import heapq
input = sys.stdin.readline

def heap_sort(arr):
    heap = []
    for i in arr:
        heapq.heappush(heap, i)
    for i in range(len(arr)):
        arr[i] = heapq.heappop(heap)
    
    return arr

n = int(input())

num_list = [int(input()) for _ in range(n)]

print('\n'.join(map(str, heap_sort(num_list))))