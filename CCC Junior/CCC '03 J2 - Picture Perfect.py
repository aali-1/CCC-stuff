import sys
from math import sqrt,ceil
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
def isprime(N):
    if N==0 or N==1: return False
    for x in range(2,ceil(sqrt(N))+1):
        if N%x==0 and N!=x:
            return False
    return True
while(True):
    thing=readint()
    if thing==0:
        break
    elif thing==1:
        print("Minimum perimeter is 4 with dimensions 1 x 1")
    elif isprime(thing):
        print(f"Minimum perimeter is {2+(2*thing)} with dimensions 1 x {thing}")
    else:
        for x in range(int(sqrt(thing)),1,-1):
            #print(x)
            if thing%x==0:
                print(f"Minimum perimeter is {(2*x)+(2*(thing//x))} with dimensions {x} x {thing//x}")
                break