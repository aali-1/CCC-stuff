import sys
low=1
high = 2*(10**9)
count=0
while(count<32):
    middle=(low+high)//2
    print(middle)
    sys.stdout.flush()
    thing=input()
    if thing=='SINKS':
        low=middle+1
    elif thing=='FLOATS':
        high=middle-1
    else:
        sys.exit()
    count+=1
print('fk')