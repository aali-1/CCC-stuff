import sys
from collections import deque
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))

thing = deque(['A','B','C','D','E'])
while(True):
    b = readint()
    n = readint()
    if b==4:
        print(*list(thing))
        sys.exit()
    elif b==1:
        for _ in range(n):
            first=thing.popleft()
            thing.append(first)
    elif b==2:
        for _ in range(n):
            last=thing.pop()
            thing.appendleft(last)
    elif b==3:
        for _ in range(n):
            first=thing.popleft()
            thing.insert(1,first)