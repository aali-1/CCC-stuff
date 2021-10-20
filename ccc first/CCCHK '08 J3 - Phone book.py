import sys
def sorting_key(item):
    return(item[1],item[0])
thing=int(sys.stdin.readline())
d={}
for _ in range(thing):
    name,number=input().split()
    d[int(number)]=name
counter=d
counter=dict.fromkeys(counter,0)
for _ in range(int(sys.stdin.readline())):
    counter[int(input())]+=1
sorte=sorted(counter.items(),key=sorting_key,reverse=True)
maxc=sorte[0][1]
strongest=0
for count in sorte:
    if count[1]<maxc:
        break
    strongest=count[0]

print(d[strongest])