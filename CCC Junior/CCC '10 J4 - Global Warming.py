import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
while(True):
    length=gi()
    if length==[0]:
        break
    length=length[1:]
    deltas=[]
    pattern=[]
    notyet=[]
    for i in range(len(length)-1):
        deltas.append(length[i+1]-length[i])
    required=None
    for i,x in enumerate(deltas):
        #print(x)
        if x==required:
            notyet.append(x)
            #print(len(notyet),len(pattern))
            required=deltas[deltas.index(required)+1]
            if len(notyet)==len(pattern):
                required=pattern[0]
            #print(notyet)
        else:
            pattern.extend(notyet)
            notyet.clear()
            try:
                required=pattern[0]
            except:
                pass
            if x==required:
                required=deltas[pattern.index(required)+1]
                notyet.append(x)            
                #print(notyet)
            else:
                pattern.append(x)
                required=pattern[0]
        #print(pattern,required)
    print(len(pattern))
    #print(deltas)