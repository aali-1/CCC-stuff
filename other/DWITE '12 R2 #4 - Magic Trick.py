import sys
input = sys.stdin.readline
for _ in range(5):
    n = int(input())
    card=[]
    ans=[]
    for i in range(n, 0, -1):
        card.append(i)
    for k in list(map(int, input().split())):
        if len(card) <= k:
            break
        ans.append(card[k])
        card.pop(k)
    if len(ans) != n:
        print('IMPOSSIBLE')
    else:
        for x in ans:
            print(x, end=' ')
        print()
