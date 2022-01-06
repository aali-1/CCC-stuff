import sys
input = sys.stdin.readline
print=sys.stdout.write
line = [int(x) for x in input().split()]
asc,dsc=False,False
for i,x in enumerate(line):
    try:
        if x > line[i+1]:
            dsc=True
        else:
            asc=True
    except(IndexError):
        pass
if asc:
    if dsc:
        print('mixed')
    else:
        print('ascending')
else:
    print('descending')