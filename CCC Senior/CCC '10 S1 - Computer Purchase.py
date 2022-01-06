import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
N=readint()
if N==0:
    sys.exit()
d={}
for x in range(N):
    name,R,S,D=readline().split()
    d[name]=(2*int(R))+(3*int(S))+int(D)
ls=sorted(d.keys())
thing=sorted(d.values())
maximum=thing[-1]
if N==1:
    print(ls[0])
    sys.exit()
maximum2=thing[-2]
for x in ls:
    if d[x]==maximum:
        print(x)
        try:
            d.pop(x)
            ls.remove(x)
        except:
            pass
        break
for x in ls:
    if d[x]==maximum2:
        print(x)
        break
        
    