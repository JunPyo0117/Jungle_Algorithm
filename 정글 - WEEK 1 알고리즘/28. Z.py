import sys

def Z(n, r, c):
    if n == 0:
        return 0

    half = 2**(n-1)
    
    if r < half and c < half:
        return Z(n-1, r, c)
    elif r < half and c >= half:
        return half*half + Z(n-1, r, c-half)
    elif r >= half and c < half:
        return 2*half*half + Z(n-1, r-half, c)
    else:
        return 3*half*half + Z(n-1, r-half, c-half)
    

input = sys.stdin.readline

N, r, c = map(int, input().split())

print(Z(N, r, c))
    