# 숫자 카드 
import sys
input = sys.stdin.readline

n = int(input().rstrip())     # n 값 입력
card = list(map(int, input().rstrip().split())) # 카드 리스트
m = int(input().rstrip())     # 값 입력
check_card = list(map(int, input().rstrip().split())) # 체크 카드 리스트

dic = {}  # 딕셔너리 선언

# 이건 왜 시간초과 나는지 모름 
# for i in check_card:
#     if i in card:
#         dic[i] = 1
#     else:
#         dic[i] = 0

# 체크카드에 있는 카드들 순서대로 딕셔너리 0으로 선언
for i in check_card:
    dic[i] = 0

# 카드리스트를 가져와서 해당 카드가 딕셔너리에 있으면 값을 1로 변경
for j in card:
    if j in dic:
        dic[j] = 1

# print(dic)
# print(dic[10])

# 딕셔너리에 있는 카드들의 값들만 출력
for k in check_card:
    print(dic[k], end=' ')


