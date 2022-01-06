import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
emp = lambda x, y: [x for _ in range(y)]

d={}

while(True):
    line=readline().split()
    d[int(line[1])]=line[0]
    if line[0]=='Waterloo':
        break
print(d[min(d.keys())])
    