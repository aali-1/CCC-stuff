import sys
input = sys.stdin.readline
word=input()[:-1]
rushhour = [[420,600],[900,1140]]
minu=int(word[:2])*60+int(word[3:])
#print(minu)
amount = 120
ans=0
while amount>0:
    if minu in list(range(420,600)) or minu in list(range(900,1140)):
        amount-=0.5
    else:
        amount-=1
    minu+=1
print(str((minu//60)%24).zfill(2),':',str(minu%60).zfill(2),sep='')