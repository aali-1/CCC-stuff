import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)+ x3 * (y1 - y2)))
def isInside(x1, y1, x2, y2, x3, y3, x, y):
    A = area (x1, y1, x2, y2, x3, y3)
    A1 = area (x, y, x2, y2, x3, y3)
    A2 = area (x1, y1, x, y, x3, y3)
    A3 = area (x1, y1, x2, y2, x, y)
    if(A == A1 + A2 + A3):
        return True
    else:
        return False
N,Q=gi()
triangles=[]
for _ in range(N):
    c=gi()
    triangles.append([c[0],c[1],c[2],c[3],c[4],c[5]])
for _ in range(Q):
    count=0
    check=gi()
    for k in range(N):
        if isInside(triangles[k][0],triangles[k][1],triangles[k][2],triangles[k][3],triangles[k][4],triangles[k][5],check[0],check[1]):
            count+=1
    print(count)