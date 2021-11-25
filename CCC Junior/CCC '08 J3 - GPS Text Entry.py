def finds(grid,c):
    for y in range(5):
        for x in range(6):
            if grid[y][x] == c:
                return [x,y]
grid = [
    ['A','B','C','D','E','F'],
    ['G','H','I','J','K','L'],
    ['M','N','O','P','Q','R'],
    ['S','T','U','V','W','X'],
    ['Y','Z',' ','-','.','_']]
currentpos = [0,0]
word = input()+'_'
ans = 0
for c in range(len(word)):
    cpos = finds(grid,word[c])
    ans += abs(cpos[0]-currentpos[0])+abs(cpos[1]-currentpos[1])
    currentpos = cpos
print(ans)
