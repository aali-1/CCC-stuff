import sys
input = sys.stdin.readline

def works(square,q):
    for x in range(2):
        if square[x]==q[x]:
            return False
        else:
            if abs(square[0]-q[0])==abs(square[1]-q[1]):
                return False
    return True

N,M=[int(x) for x in input().split()]
queens=[[int(x) for x in input().split()] for _ in range(M)]
count=0

for i in range(1,N+1):
    for j in range(1,N+1):
        found=False
        for q in queens:
            if not works([i,j],q):
                found=False
                break
            else:
                found=True
        if found:
            #print(i,j)
            count+=1
print(count)