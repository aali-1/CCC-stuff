import sys
from math import ceil
M,N,K = [int(x) for x in sys.stdin.readline().split()]
heights = [int(x) for x in sys.stdin.readline().split()]
amt = 0
colreq = ceil(K/M)
heights.sort(reverse=True)
f = min(M,K)
rowone = heights[:colreq]
#heights= heights[colreq:]
#h = 0
for x in range(len(rowone)):
    for y in range(f-1):
        try:
            amt+=rowone[x]-heights[colreq]+y+1
            colreq+=1
        except(IndexError):
            pass
    if colreq>len(heights):
        break
print(amt)
'''
3 7 5
250 200 150 100 50
'''
