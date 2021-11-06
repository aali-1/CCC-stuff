import sys
def check(a,b):
    a=[int(x) for x in str(a)]
    b=[int(x) for x in str(b)]
    if len(a)!=len(b):
        return False
    a.sort()
    b.sort()
    if a!=b:
        return False
    else:
        return True
nb = int(sys.stdin.readline())
ans=[0]
for x in range(nb+1,1*(10**len(str(nb)))):
    if check(x,nb):
        print(x)
        sys.exit()
print(0)

