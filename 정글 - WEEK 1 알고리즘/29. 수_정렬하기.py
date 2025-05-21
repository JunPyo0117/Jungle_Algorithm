import sys
input = sys.stdin.readline

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 교환이 일어났는지 확인하는 플래그
        swapped = 0
        # 마지막 i개의 요소는 이미 제자리에 있으므로 검사하지 않음
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped += 1
        
        # 교환이 일어나지 않았다면 정렬이 완료된 것
        if swapped ==0:
            break
    
    return print('\n'.join(map(str, arr)))

n = int(input())

num_list = [int(input()) for i in range(n)]

bubble_sort(num_list)