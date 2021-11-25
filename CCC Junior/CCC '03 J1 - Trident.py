import sys
t,s,h = int(sys.stdin.readline()),int(sys.stdin.readline()),int(sys.stdin.readline())
for _ in range(t):
    print('*'+' '*s+'*'+' '*s+'*')
print('*'*(3+(2*s)))
for _ in range(h):
    print(' '*(1+s)+'*')