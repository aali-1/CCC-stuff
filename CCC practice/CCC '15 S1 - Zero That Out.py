import sys
K=int(sys.stdin.readline())
values = []
for _ in range(K):
    money=int(sys.stdin.readline())
    if money==0:
        values.pop()
    else:
        values.append(money)
print(sum(values))

