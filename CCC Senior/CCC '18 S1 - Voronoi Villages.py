import sys
input = sys.stdin.readline
n=int(input())
things = sorted([int(input()) for x in range(n)])
smallest=100000000000000000000000000000
for i in range(1,n-1):
    nb=((things[i]-things[i-1])/2)+((things[i+1]-things[i])/2)
    smallest=min(nb,smallest)
print(smallest)