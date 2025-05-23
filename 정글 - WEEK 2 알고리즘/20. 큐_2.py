import sys 
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push':  # push
        queue.append(int(command[1]))
    elif command[0] == 'pop':  # pop
        print(queue.popleft() if queue else -1)
    elif command[0] == 'size':  # size
        print(len(queue))
    elif command[0] == 'empty':  # empty
        print(1 if not queue else 0)
    elif command[0] == 'front':  # front
        print(queue[0] if queue else -1)
    elif command[0] == 'back':
        print(queue[-1] if queue else -1)