import sys
N = int(sys.stdin.readline())
A = [int(s) for s in sys.stdin.readline().split()]
#possible_cards=list(range(1,max(A)+2))
if A[0]==0:
    what = list(filter(lambda a: a != 0, A.copy()))
    if len(what)==0:
        raise SystemExit(print('YES'))
    possible_cards=list(range(1,min(what)+1))
else:
    try:
        first=A.index(0)
    except(ValueError):
        if A==sorted(A):
            raise SystemExit(print('YES'))
        else:
            raise SystemExit(print('NO'))
    other=first-1
    for x in range(first,len(A)):
        if A[x]>0:
            other=x
            break
    possible_cards=list(range(A[first-1],A[other]+1))
#print(possible_cards)    
for x in possible_cards:
    thing = A.copy()
    thing = [x if y==0 else y for y in thing]
    if thing==sorted(thing):
        raise SystemExit(print('YES'))
print('NO')



