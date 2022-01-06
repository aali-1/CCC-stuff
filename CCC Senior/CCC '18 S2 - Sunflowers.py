import sys
input=sys.stdin.readline

def rotate(ls,n):
    what=[x[:] for x in ls]
    for y in range(n):
        for x in range(n):
            ls[y][x]=what[n-1-x][y]
    return ls

def works(ls,n):
    for i in range(n-1):
        for j in range(n-1):
            if ls[i][j]>ls[i+1][j]:
                return False
    for x in ls:
        if x !=sorted(x):
            return False
    return True

def prnt(ls):
    for x in ls:
        print(*x)    

n=int(input())
all=[[int(x) for x in input().split()] for y in range(n)]
if works(all,n):
    prnt(all)
else:
    for _ in range(4):
        all = rotate(all,n)
        if works(all,n):
            prnt(all)
            sys.exit()