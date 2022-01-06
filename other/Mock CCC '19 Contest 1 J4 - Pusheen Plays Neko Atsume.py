import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))

from collections import defaultdict
N=readint()
d=defaultdict(lambda: 0)
for _ in range(N):
    thing=readline()
    d[thing]+=1
vals=d.values()
p=defaultdict(lambda: [])
p[d['Deluxe Tuna Bitz']].append('Deluxe Tuna Bitz')
p[d['Bonito Bitz']].append('Bonito Bitz')
p[d['Sashimi']].append('Sashimi')
p[d['Ritzy Bitz']].append('Ritzy Bitz')
now=sorted(p.keys(),reverse=True)
#print(p)
for x in now:
    if x>0:
        for y in p[x]:
            print(y,x)