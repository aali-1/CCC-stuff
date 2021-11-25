import sys
x, y = [int(x) for x in sys.stdin.readline().split()]
grid = []
for _ in range(x):
  grid.append(list(sys.stdin.readline())[:y])
for z in range(x-1):
  for v in range(y-1):
    if grid[z][v]=='.':
      thing=0
      if z!=0:
        try:
          if grid[z-1][v]=='.':
            thing+=1
        except(IndexError):
          pass
      try:
        if grid[z+1][v]=='.':
          thing+=1
      except(IndexError):
        pass
      if v!=0:
        try:
          if grid[z][v-1]=='.':
            thing+=1
        except(IndexError):
          pass
      try:
        if grid[z][v+1]=='.':
          thing+=1
      except(IndexError):
        pass
      if thing<2:
        print(1)
        sys.exit()
print(0)