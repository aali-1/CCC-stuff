import sys
from functools import reduce
input = sys.stdin.readline
def fits(x,y):
    x.sort(reverse=True)
    y.sort(reverse=True)
    for z in range(3):
        if x[z]>y[z]:
            return False
    return True
n=int(input())
boxes=[]
for _ in range(n):
    f=[int(x) for x in input().split()]
    boxes.append(f)
boxes.sort(key=lambda d: reduce(lambda x, y: x * y, d)) #sort based on volume
for _ in range(int(input())):
    found=False
    y=[int(x) for x in input().split()]
    for z in range(n):
        if fits(y,boxes[z]):
            found=True
            print(eval(str(tuple(boxes[z])).replace(',','*')))
            break
    if not found:
        print('Item does not fit.')
