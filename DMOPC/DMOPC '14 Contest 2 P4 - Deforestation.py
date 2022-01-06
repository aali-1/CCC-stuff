import sys
input = sys.stdin.readline
N=int(input())
thing=[0]*(N+1)
for x in range(1,N+1):
    thing[x]=int(input())+thing[x-1]
print(thing)
for _ in range(int(input())):
    one,two=[int(x) for x in input().split()]
    print(thing[two+1]-thing[one])