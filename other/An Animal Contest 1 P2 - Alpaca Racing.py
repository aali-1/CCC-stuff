import sys; input = sys.stdin.readline
from math import floor
alpacas,distance,K,X, = [int(x) for x in input().split()]
def func(speed,X):
  return(speed*((100-X) * 0.01))
speeds = []
for _ in range(alpacas):
  thing = int(input())
  speeds.append(thing)
P = int(input())
count=0
#print(speeds,amount)
for x in range(alpacas):
  while speeds[x]>=P:
    speeds[x] = floor(func(speeds[x],X))
    #print(speeds[x])
    count+=1
    if count>K:
      print('NO')
      sys.exit()
print('YES')