import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
N=readint()
grid=[]
for _ in range(N):
    word=[x for x in readline()]
    if len(set(word))==N:
        grid.append(word)
    else:
        raise SystemExit(print('No'))
for x in range(N):
    if len(set([grid[x][y] for y in range(N)]))==N:
        continue
    else:
        raise SystemExit(print('No'))
if sorted(grid[0])==grid[0]:
    if sorted([grid[x][0] for x in range(N)]) == [grid[x][0] for x in range(N)]:
        print('Reduced')
    else:
        print('Latin')
else:
    print('Latin')