import sys
x=sorted([int(x) for x in sys.stdin.readline().split()],reverse=True)
y=sorted([int(x) for x in sys.stdin.readline().split()],reverse=True)
for z in range(3):
    if x[z]>y[z]:
        print('N')
        sys.exit()
print('Y')

