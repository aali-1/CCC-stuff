import sys
input = sys.stdin.readline
one,two = [int(x) for x in input().split()]
while one!=0:
    temp=one
    one=one//2
    if abs(temp-two)<abs(one-two):
        raise SystemExit(print(temp))