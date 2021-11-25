import sys; input, print = sys.stdin.readline, sys.stdout.write
distance = int(input())
n = int(input())
clubs = [int(input()) for x in range(n)]
values=[0]
founder = [False for i in range(5281)]
newvalues = []
counter=0
while True:
    for x in range(len(values)):
        for y in range(n):
            thing = values[x]+clubs[y]
            if thing<distance and not founder[thing]:
                  founder[thing]=True
                  newvalues.append(thing)
            elif thing == distance:
                  counter+=1
                  print(f"Roberta wins in {counter} strokes.")
                  sys.exit()
    counter+=1
    values.clear()
    values=newvalues.copy()
    newvalues.clear()
    if len(values)==0:
        print('Roberta acknowledges defeat.')
        break
'''
100
3
3
3
3
'''