import sys
input = sys.stdin.readline

k={x:None for x in range(1,9)}
#print(k)

pinepoints=0
bluepoints=0

n=int(input())

for _ in range(n):
  sec,a,b=[int(x) for x in input().split()]
  if a <=4:
    if b>4:
      if k[a]!= None and sec-k[a]<=10:
        pinepoints+=50
      pinepoints+=100
    else:
      pinepoints-=100
  else:
    if b<=4:
      if k[a]!= None and sec-k[a]<=10:
        bluepoints+=50
      bluepoints+=100
    else:
      bluepoints-=100
  k[a]=sec
print(pinepoints,bluepoints)
