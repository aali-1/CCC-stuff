import sys
input = sys.stdin.readline
N = int(input())
d={}
for x in range(N):
  Y,x = input().split()
  d[x]=Y
thing = input()[:-1]
while len(thing)>0:
  for x in d:
    if thing[:len(x)]==x:
      thing=thing[len(x):]
      #print(thing)
      print(d[x],end='')
