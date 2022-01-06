import sys
input=sys.stdin.readline
ls=[1234, 111, 123, 135, 147, 159, 210, 222, 234, 246, 258, 321, 333, 345, 357, 420, 432, 444, 456, 531, 543, 555, 630, 642, 654, 741, 753, 840, 852, 951, 1111]
N=int(input())
ans=0
ans+=(31*(N//720))
new=str(((12+N//60)-1)%12+1)+str(N%60).rjust(2,'0')
if int(new)>=1200:
    if int(new)>=1234:
        ans+=1
else:
    new=int(new)
    ans+=1
    for x in range(1,31):
        if new>=ls[x]:
            ans+=1
print(ans)
