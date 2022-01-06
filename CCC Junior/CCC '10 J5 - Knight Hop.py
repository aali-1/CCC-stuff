import sys
visited = [[False for i in range(9)] for j in range(9)]
input = sys.stdin.readline

def works(x):
    if any(i<=0 for i in x) or any(i>8 for i in x):
        return False
    elif visited[x[0]][x[1]]==True:
        return False
    return True

start = [int(x) for x in input().split()]
end = [int(x) for x in input().split()]
visited[start[0]][start[1]]=True
count = 0
values = [start]
newvalues=[]
while count<7:
    if end in values:
        print(count)
        break
    for i in range(len(values)):
        x = values[i][0]
        y = values[i][1]
        newvalues.append([x+1,y+2])
        newvalues.append([x+1,y-2])
        newvalues.append([x-1,y+2])
        newvalues.append([x-1,y-2])
        newvalues.append([x+2,y+1])
        newvalues.append([x+2,y-1])
        newvalues.append([x-2,y+1])
        newvalues.append([x-2,y-1])
        
    newvalues = [x for x in newvalues if works(x)]
    
    for x in newvalues:
        try:
            visited[x[0]][x[1]]=True
        except(IndexError):
            pass
        
    values.clear()
    values = newvalues.copy()
    newvalues.clear()
    count+=1
    