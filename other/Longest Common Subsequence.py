import sys
input = sys.stdin.readline
N,M=[int(x) for x in input().split()]
one=input().split()
two=input().split()
def lcs(one,two):
   grid=[[0 for x in range(M+1)] for x in range (N+1)]
   for i in range(N):
      for j in range(M):
         if one[i]==two[j]:
            grid[i+1][j+1]=grid[i][j]+1
         else:
            grid[i+1][j+1]=max(grid[i][j+1],grid[i+1][j])
   return grid[-1][-1]           
print(lcs(one,two))