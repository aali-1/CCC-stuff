import sys
input = sys.stdin.readline
scale = int(input())
for x in range(scale):
    print('*'*scale,'x'*scale,'*'*scale,sep='')
for x in range(scale):
    print(' '*scale,'x'*scale,'x'*scale,sep='')
for x in range(scale):
    print('*'*scale,' '*scale,'*'*scale,sep='')   