import sys
N,Q=[int(x) for x in sys.stdin.readline().split()]
ratings=[0]+[int(x) for x in sys.stdin.readline().split()]
for x in range(1,N+1):
    ratings[x]+=ratings[x-1] #PREFIX SUM ARRAY CODE
for _ in range(Q):
    a,b = map(int,sys.stdin.readline().split())
    print(ratings[-1]-ratings[b]+ratings[a-1])

'''
10 3
5 6 7 8 3 4 5 6 1 2
1 3
2 4
1 10
'''