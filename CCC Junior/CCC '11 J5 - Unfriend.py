import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))

from collections import defaultdict
graph=defaultdict(lambda: [])
N=readint()
for x in range(N-1):
    num=readint()
    graph[num].append(x+1)
#print(graph)
def recursion(x):
    result=1
    for y in graph[x]:
        result*=(1 + recursion(y))
    return result
print(recursion(N))