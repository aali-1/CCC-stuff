import sys
N = int(sys.stdin.readline())
things = []
for _ in range(N):
  things.append(int(sys.stdin.readline()))
things.sort()
solution = 0
for i in range(N):
    solution+=things[i]*things[(i*-1)-1]
print(solution%10007)
