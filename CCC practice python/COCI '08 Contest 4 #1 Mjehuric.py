import sys
unsort = [int(x) for x in sys.stdin.readline().split()]
while unsort!=[1,2,3,4,5]:
    if unsort[0]>unsort[1]:
        u1=unsort[1]
        unsort[1]=unsort[0]
        unsort[0]=u1
        print(' '.join(list(map(str,unsort))))
    if unsort[1]>unsort[2]:
        u2=unsort[2]
        unsort[2]=unsort[1]
        unsort[1]=u2
        print(' '.join(list(map(str,unsort))))
    if unsort[2]>unsort[3]:
        u2=unsort[3]
        unsort[3]=unsort[2]
        unsort[2]=u2
        print(' '.join(list(map(str,unsort))))
    if unsort[3]>unsort[4]:
        u2=unsort[4]
        unsort[4]=unsort[3]
        unsort[3]=u2
        print(' '.join(list(map(str,unsort))))