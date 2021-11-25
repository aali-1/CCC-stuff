highest = 0
for x in range(int(input())):
    y=eval(str(tuple([int(x) for x in input().split()])).replace(',','*'))
    if y>highest:
        highest=y
rhighest = 0
for x in range(int(input())):
    y=eval(str(tuple([int(x) for x in input().split()])).replace(',','*'))
    if y>rhighest:
        rhighest=y
if rhighest>highest:
    print('Natalie')
elif highest>rhighest:
    print('Casper')
else:
    print('Tie')