import sys
input = sys.stdin.readline
N = int(input())
ans=0
for i in range(N+1):
    ans+=i*2
#print(ans)
for i in range(N+1):
    for j in range(i):
        ans+=i+j
print(ans)