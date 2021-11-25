import sys
for _ in range(int(input())):
    noun,verb,object = int(sys.stdin.readline()),int(sys.stdin.readline()),int(sys.stdin.readline()),
    nouns=[]
    verbs=[]
    objects=[]
    for _ in range(noun):
        nouns.append(input())
    for _ in range(verb):
        verbs.append(input())
    for _ in range(object):
        objects.append(input())
    for x in nouns:
        for y in verbs:
            for z in objects:
                print(x,y,z+'.')