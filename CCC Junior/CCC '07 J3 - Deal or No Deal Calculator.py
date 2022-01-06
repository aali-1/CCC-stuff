import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
d={1:100,2:500,3:1000,4:5000,5:10000,6:25000,7:50000,8:100000,9:500000,10:1000000}
n=readint()
for _ in range(n):
    d.pop(readint())
value=readint()*len(d)
avg=sum(d.values())
if value>avg:
    sys.stdout.write('deal')
else:
    sys.stdout.write('no deal')