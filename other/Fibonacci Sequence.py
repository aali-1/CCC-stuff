import sys
from functools import cache
sys.setrecursionlimit(10**19)

@cache
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(int(input()))%1000000007)