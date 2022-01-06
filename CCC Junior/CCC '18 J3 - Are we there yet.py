import sys
input = sys.stdin.readline
distances = [0]+[int(x) for x in input().split()]
for i in range(1,5):
    distances[i]+=distances[i-1]
print(*distances)
for i in range(1,5):
    thing=int(distances[i])
    for j,x in enumerate(distances):
        #print(thing)
        if j<i:
            distances[j]=x+thing
        elif j==i:
            distances[j]=0
        elif j>i:
            distances[j]=x-thing
    print(*distances)