import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
from itertools import permutations
word=sorted(readline())
things=sorted(list(permutations(word)))
for x in things:
    print(''.join(x))