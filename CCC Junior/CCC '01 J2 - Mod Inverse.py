import sys
x,m=int(sys.stdin.readline()),int(sys.stdin.readline())
found=False
for y in range(m+1):
    if (y*x)%m==1:
        print(y)
        found=True
        break
if not found:
    print('No such integer exists.')
