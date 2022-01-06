import sys
input=sys.stdin.readline
print=sys.stdout.write
line = input()[:-1]
happy,sad=0,0
for i,c in enumerate(line):
    try:
        if c==':' and line[i+1]=='-':
            if line[i+2]==')':
                happy+=1
            elif line[i+2]=='(':
                sad+=1
    except(IndexError):
        pass
if happy>sad:
    print('happy')
elif sad>happy:
    print('sad')
elif happy==0 and sad==0:
    print('none')
else:
    print('unsure')