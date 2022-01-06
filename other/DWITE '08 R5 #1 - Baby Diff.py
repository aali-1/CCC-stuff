import sys
input = sys.stdin.readline
for _ in range(5):
    one = input()[:-1]
    two=input()[:-1]
    ans=0
    for i in range(min(len(one),len(two))):
        if one[i]==two[i]:
            ans+=1
        else:
            break
    print(ans)