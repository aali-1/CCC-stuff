import sys
input = sys.stdin.readline
d={}
J,A=int(input()),int(input())
ans=0
for i in range(1,J+1):
    d[i]=input()[0]
for _ in range(A):
    size,number = input().split()
    number=int(number)
    if size=='L':
        if d[number]=='L':
            ans+=1
            d[number]=-1
            continue
    elif size=='M':
        if d[number]=='M':
            ans+=1
            d[number]=-1
            continue
        if d[number]=='L':
            ans+=1
            d[number]=-1
            continue
    else:
        if d[number]=='S':
            ans+=1
            d[number]=-1
            continue
        if d[number]=='M':
            ans+=1
            d[number]=-1
            continue
        if d[number]=='L':
            ans+=1
            d[number]=-1
            continue
print(ans)