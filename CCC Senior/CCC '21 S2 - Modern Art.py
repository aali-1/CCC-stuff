import sys
input = sys.stdin.readline
M,N,K = int(input()),int(input()),int(input())
rows = [0 for i in range(M)]
cols = [0 for i in range(N)]
for _ in range(K):
    thing, num = input().split()
    num = int(num)-1
    if thing == 'R':
        rows[num]+=1
    else:
        cols[num]+=1
count = 0
for y in range(M):
    for x in range(N):
        if (rows[y]+cols[x])%2==1:
            count+=1
print(count)