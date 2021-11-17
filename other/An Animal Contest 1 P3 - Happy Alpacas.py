N,X=[int(x) for x in input().split()]
if (N-X)%2!=0 or X>N:
    print(-1)
else:
    alpacas=[0]*N
    num=(N-X)/2
    for x in range(int(num)):
        alpacas[x*2]=1
    print(*alpacas,sep=" ")