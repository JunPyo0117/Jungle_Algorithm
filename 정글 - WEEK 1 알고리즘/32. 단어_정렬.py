import sys
input = sys.stdin.readline

n = int(input())
string_list = [input().strip() for i in range(n)]

string_list = list(set(string_list))
string_list.sort()
string_list.sort(key=len)

print('\n'.join(string_list))