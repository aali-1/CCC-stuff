#this doesnt work lol
import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
l=readint()
w=readint()
grid=[['.' for i in range(l)] for j in range(w)]
rl=readint()
rw=readint()
for i in range(rw):
    for j in range(rl):
        grid[i][j]='-'
        grid[-(i+1)][j]='-'
        grid[-(i+1)][-(j+1)]='-'
        grid[i][-(j+1)]='-'
for i in range(len(grid)):
    grid[i].append('-')
grid.append(['-']*l)
print(*grid,sep='\n')
coord=[0,rl]
for _ in range(readint()):
    grid[coord[0]][coord[1]]='-'
    try:
        if grid[coord[0]][coord[1]+1]=='.':
            coord=[coord[0],coord[1]+1]
        elif grid[coord[0]+1][coord[1]]=='.':
            coord=[coord[0]+1,coord[1]]
        elif grid[coord[0]][coord[1]-1]=='.':
            coord=[coord[0],coord[1]-1]
        elif grid[coord[0]-1][coord[1]]:
            coord=[coord[0]-1,coord[1]]
        else:
            coord[0]+=1
            coord[1]+=1
            print(*coord,sep='\n')
            sys.exit()
        print(coord,end=' ')
    except:
        print(coord)
coord[0]+=1
coord[1]+=1
print(*coord,sep='\n')

    