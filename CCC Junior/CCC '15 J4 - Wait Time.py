import sys
input = sys.stdin.readline

rd={}
times={}

time=0
for _ in range(int(input())):
    command,num=input().split()
    num=int(num)
    if command=='R':
        rd[num]=time
    elif command=='S':
        try:
            times[num]+=time-rd[num]
            rd[num]=None
        except(KeyError):
            times[num]=time-rd[num]
            rd[num]=None
    else:
        time+=num-2
    time+=1
for x in rd:
    if rd[x]!=None:
        times[x]=-1
thing=sorted(list(times.keys()))
for x in thing:
    print(x,times[x])