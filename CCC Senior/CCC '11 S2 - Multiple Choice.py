import sys
input=sys.stdin.readline
ans=[]
count=0
lins=int(input())
for x in range(lins):
    ans.append(input()[0])
for x in range(lins):
    if input()[0]==ans[x]:
        count+=1
print(count)