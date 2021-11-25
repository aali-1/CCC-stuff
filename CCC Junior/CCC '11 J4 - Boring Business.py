import sys
input = sys.stdin.readline
unsafe=[[0, -1], [0, -2], [0, -3], [1, -3], [2, -3], [3, -3], [3, -4], [3, -5], [4, -5], [5, -5], [5, -4], [5, -3], [6, -3], [7, -3], [7, -4], [7, -5], [7, -6], [7, -7], [6, -7], [5, -7], [4, -7], [3, -7], [2, -7], [1, -7], [0, -7], [-1, -7], [-1, -6], [-1, -5]]
pos = [-1,-5]
thing = '.'
outputs = []
while thing != 'DANGER':
    direction, num = input().split()
    num= int(num)
    thing = 'safe'
    if direction == 'q':
        break
    elif direction == 'l':
        for _ in range(num):
            pos[0]-=1
            if pos in unsafe:
                thing = 'DANGER'
            unsafe.append([pos[0],pos[1]])
    elif direction == 'r':
        for _ in range(num):
            pos[0]+=1
            if pos in unsafe:
                thing = 'DANGER'
            unsafe.append([pos[0],pos[1]])
    elif direction == 'u':
        for _ in range(num):
            pos[1]+=1
            if pos in unsafe:
                thing = 'DANGER'
            unsafe.append([pos[0],pos[1]])
    else:
        for _ in range(num):
            pos[1]-=1
            if pos in unsafe:
                thing = 'DANGER'
            unsafe.append([pos[0],pos[1]])
    print(*pos,thing,sep=' ')