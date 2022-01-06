import sys
input = sys.stdin.readline
L=int(input())
#print(ls)
maximum=0
current=0
N=int(input())
alligators=sorted([[int(x) for x in input().split()] for _ in range(N)],key=lambda x: (x[0]))
#print(alligators)
maximum=max(maximum,min(map(min,alligators)),L-max(map(max, alligators)))
for y in range(N):
    if alligators[y][0]>current and alligators[y][0]-current>maximum:
        maximum=alligators[y][0]-current
    if current<alligators[y][1]:
        current=alligators[y][1]
print(maximum)
