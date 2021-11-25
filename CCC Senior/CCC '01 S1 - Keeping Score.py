import sys
input = sys.stdin.readline
points = {'C':0,'D':0,'H':0,'S':0}
cards = {'C':[],'D':[],'H':[],'S':[]}
everything = input()[:-1]
for h in range(len(everything)):
    if everything[h] in ['D','H','S','C']:
        start = everything[h]
    else:
        cards[str(start)].append(everything[h])
#print(cards)    
for x in cards:
    if len(cards[x])==2:
        points[x]+=1
    elif len(cards[x])==1:
        points[x]+=2
    elif len(cards[x])==0:
        points[x]+=3
    for y in cards[x]:
        if y=='A':
            points[x]+=4
        elif y=='K':
            points[x]+=3
        elif y=='Q':
            points[x]+=2
        elif y=='J':
            points[x]+=1
print('Cards Dealt Points')
print('Clubs', end=' ')
print(*cards['C'],points['C'])
print('Diamonds', end=' ')
print(*cards['D'],points['D'])
print('Hearts', end=' ')
print(*cards['H'],points['H'])               
print('Spades', end=' ')
print(*cards['S'],points['S'])
print('Total',sum(list(points.values())))