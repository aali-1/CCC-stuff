import sys
input = sys.stdin.readline
thing = input()[:-1]
vop = bool(thing.count('V')%2)
hop = bool(thing.count('H')%2)
#print(vop,hop)
ls = [[1,2],[3,4]]
if vop:
    ls=[[2,1],[4,3]]
if hop:
    if vop:
        ls=[[4,3],[2,1]]
    else:
        ls = [[3,4],[1,2]]
for x in ls:
    print(*x)