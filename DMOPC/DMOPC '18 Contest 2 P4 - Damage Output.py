import sys
input = sys.stdin.readline
N,M=[int(x) for x in input().split()]
ratings=[0]+[int(x) for x in input().split()]
for x in range(1,N+1):
    ratings[x]+=ratings[x-1]
#print(ratings)
one = 0
two = 0
thing = N+1
for i in range(N*2+2):
    try:
        sm=ratings[two]-ratings[one]
    except(IndexError):
        raise SystemExit(print(thing))
    #print(sm,one,two)
    if sm<M:
        if N==two-one:
            raise SystemExit(print(-1))
        else:
            two+=1
    else:
        thing = min(thing,two-one)
        one +=1

        