# 프린터 큐
# 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
# 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄
# 3
# 1 0
# 5
# 4 2
# 1 2 3 4
# 6 0
# 1 1 9 1 1 1 왜 5번쨰인지 모르겠음 
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for i in range(n):
    paper, m = map(int, input().split())
    a_list = deque()
    a_list = list(map(int, input().split()))
    # print(paper, m, a_list)
