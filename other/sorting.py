import sys
N = int(sys.stdin.readline())
ls = []
for _ in range(N):
    ls.append(int(sys.stdin.readline()))
print('\n'.join(map(str,sorted(ls))))
#for x in sorted(ls):
#    print(x)
