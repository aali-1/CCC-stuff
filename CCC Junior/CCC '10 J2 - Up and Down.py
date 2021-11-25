import sys
input = sys.stdin.readline
a,b,c,d,s = int(input()),int(input()),int(input()),int(input()),int(input())
def by(a,b,s):
    byr=0
    moves =0;
    while(True):
        if moves+a<=s:
            moves+=a
            byr+=a
        else:
            temp=moves
            moves+=s-temp
            byr+=s-temp
        if moves==s:
            break
        if moves+b<=s:
            moves+=b
            byr-=b
        else:
            temp=moves
            moves+=s-temp
            byr-=s-temp
        if moves==s:
            break
    return byr
Nikky = by(a,b,s)
byron = by(c,d,s)
if byron>Nikky:
    print('Byron')
elif Nikky>byron:
    print('Nikky')
else:
    print('Tied')
'''
20
10
21
10
21
'''