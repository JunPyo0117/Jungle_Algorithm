# 문자열 폭발
import sys
input = sys.stdin.readline

# \n 제거
my_string = input().rstrip()   
boom = input().rstrip()

# 시간 초과 ㅋㅋㅋㅋ
# for _ in range(len(my_string)):
#     my_string = my_string.replace(boom, '')

# 스택 선언
stack = []        
boom_chk = []

for s in my_string:
    stack.append(s) # 스택에 한글자씩 append
    if len(stack) >= len(boom):  # 스택의 길이와 폭탄이 길이를 비교
        boom_chk = stack[len(stack)-len(boom):]  # 붐체크는 슬라이스를 통해 [스택 - 붐]을 찾아서 배열에 저장 
        # print(stack)
        # print(boom_chk)
        if ''.join(boom_chk) == boom: # 만약 붐체크가 폭탄에 있는 글이랑 같아진다면 조건 만족
            for _ in range(len(boom)): # 포탄의 길이만큼 팝해주면 스택에 쌓인 폭탄이 제거됨
                stack.pop()


if not stack: # 스택이 비어있으면 폭탄이 다 터짐
    print("FRULA")
else:   # 스택이 있으면 폭탄이 터지고 남은 문자 출력
    print(''.join(stack))

