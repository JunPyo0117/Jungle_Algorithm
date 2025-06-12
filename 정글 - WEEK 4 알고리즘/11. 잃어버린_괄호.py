import sys
input = sys.stdin.readline

num = input().strip()

# num = num.replace('-', ' ')
num = num.split('-')

parts = []
num_list = []
subnum = 0
for i in num:
    parts = i.split('+')
    subnum = sum(map(int, parts))
    num_list.append(subnum)

result = num_list[0] - sum(num_list[1:])
print(result)


    
