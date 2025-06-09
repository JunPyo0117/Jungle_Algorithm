import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    cnt = 1
    applicant = []
    n = int(input())
    n_list = [list(map(int, input().split())) for _ in range(n)]
    n_list.sort()
    
    for document, interview in n_list:
        if not applicant:
            applicant.append((document, interview))
            standard = interview
        elif standard > interview:
            applicant.append((document, interview))
            standard = interview

    print(len(applicant))
    