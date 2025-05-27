a, b, c = map(int, input().split())

def pow(a,b):
    if b == 1:
        return a%c
    temp = pow(a,b//2)
    if b % 2 == 0:
        return(temp*temp) %c
    else:
        return(temp*temp *a) %c
    
print(pow(a,b))

# 모듈러의 연산의 성질
# 곱하고 나머지를 구하나 나머지끼리 곱하고 다시 나머지를 구하나 값은 같다.
# 1. (a+b) mod n = [(a mod n)+(b mod n)] mod n 
# 2. (a*b) mod n = [(a mod n)*(b mod n)] mod n
