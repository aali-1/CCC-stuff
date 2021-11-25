import sys
def neighbours(i, j):
    
    return [[i-1],[j],[i],[j-1],[i+1],[j],[i],[j+1]]

floors,r,h=int(sys.stdin.readline()),int(sys.stdin.readline()),int(sys.stdin.readline())
grid=[]
for _ in range(r):
    grid.append(list(sys.stdin.readline()[:-1]))
boxes=0
for x in range(r):
    for y in range(h):
        if grid[x][y]=='.':
            print(x,y)
            boxes+=1
            grid[x][y]='p'
            if grid[x+1][y]=='.':
                grid[x+1][y]='p'
            if grid[x][y+1]=='.':
                grid[x][y+1]='p'
        if grid[x][y]=='p':
            if grid[x+1][y]=='.':
                grid[x+1][y]='p'
            if grid[x][y+1]=='.':
                grid[x][y+1]='p'
for x in grid:
    print(x)
print(boxes)