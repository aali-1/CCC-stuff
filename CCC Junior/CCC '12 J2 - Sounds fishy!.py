import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
things=[readint() for _ in range(4)]
if len(set(things))>1 and len(set(things))<4:
    print('No Fish')
    sys.exit()
if things==sorted(things):
    if len(set(things))==1:
        print('Fish At Constant Depth')
    else:
        print('Fish Rising')
elif things==sorted(things,reverse=True):
    print('Fish Diving')
else:
    print('No Fish')