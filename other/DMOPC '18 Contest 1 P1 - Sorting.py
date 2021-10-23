import sys
N = int(sys.stdin.readline())
A = [int(s) for s in sys.stdin.readline().split()]
found = False
try:
    first_zero=A.index(0)
except ValueError:
    print('NO')
    found = True
if not found:
    last_zero=len(A)-A[::-1].index(0)-1
    rangeone=None;rangetwo=None;
    rangeone = 0 if first_zero==0 else first_zero-1
    rangetwo = A.index(max(A)) if last_zero==len(A)-1 else last_zero+1
    for x in range(A[rangeone]+1,A[rangetwo]+1):
        a=A
        if [x if y==1 else y for y in a] == sorted([x if y==1 else y for y in a]):
            print("YES")
            found = True
    if not found:
        print('NO')
        
        



