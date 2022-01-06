import sys
input = sys.stdin.readline
sentence=""
f={'t':0,'s':0}
for _ in range(int(input())):
    word=input().lower()
    f['t']+=word.count('t')
    f['s']+=word.count('s')
if f['t']>f['s']:
    print('English')
else:
    print('French')