import sys
from functools import reduce
def fits(x,y):
    x.sort(reverse=True)
    y.sort(reverse=True)
    for z in range(3):
        if x[z]>y[z]:
            return False
    return True
n=int(sys.stdin.readline())
boxes=[]
for _ in range(n):
    f=[int(x) for x in sys.stdin.readline().split()]
    boxes.append(f)
boxes.sort(key=lambda d: reduce(lambda x, y: x * y, d))
for _ in range(int(sys.stdin.readline())):
    found=False
    y=[int(x) for x in sys.stdin.readline().split()]
    for z in range(n):
        if fits(y,boxes[z]):
            found=True
            print(eval(str(tuple(boxes[z])).replace(',','*')))
            break
    if not found:
        print('Item does not fit.')
    
    
'''
3
1 2 3
3 4 5
2 3 4
1
1 1 1

'''
