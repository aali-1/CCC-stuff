import sys
real = [['A','B','C','D'],['E','F','G','H'],['I','J','K','L'],['M','N','O','.']]
fake=[]
def man_dist(a,b,c,d):
    return abs(c-a)+abs(d-b)
def find(j,i):
    for y in range(4):
        for x in range(4):
            if j[y][x]==i:
                return [x,y]
for _ in range(4):
    fake.append(sys.stdin.readline())
ans=0
for y in range(4):
    for x in range(4):
        if real[y][x]!=fake[y][x] and fake[y][x]!='.':
            h=fake[y][x]
            realpos = find(real,h)
            ans+=(man_dist(x,y,realpos[0],realpos[1]))
print(ans)

