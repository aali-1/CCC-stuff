import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))

from collections import deque
queue=deque()
R=readint()
L=readint()
grid=[gi() for _ in range(R)]
queue.append(grid[0])
queue2=deque()
for i in range(R-1):
    #print(queue)
    queue=deque(set(tuple(x) for x in queue))
    for x in queue:
        thing=grid[i+1]
        what=[x[y] ^ thing[y] for y in range(L)]
        queue2.append([x[y] ^ thing[y] for y in range(L)])
        queue2.append(thing)
    queue.clear()
    queue=queue2.copy()
    queue2.clear()
#print(queue)
print(len(set(tuple(x) for x in queue)))
