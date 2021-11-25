import sys
input = sys.stdin.readline
names=[]
bids=[]
for _ in range(int(input())):
    name = input()[:-1]
    value = int(input())
    names.append(name)
    bids.append(value)
for x in range(len(names)):
    if bids[x] == max(bids):
        print(names[x])
        sys.exit()    