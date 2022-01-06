import sys
input = sys.stdin.readline
for _ in range(5):
    found=False
    word=input()[:-1]
    prefixes,suffixes=[''],['']
    for x in range(1,len(word)+1):
        prefixes.append(prefixes[x-1]+word[x-1])
    for x in range(1,len(word)+1):
        suffixes.append(word[-(x)]+suffixes[x-1])
        #print(suffixes)
    suffixes=suffixes[1:-1]
    prefixes=prefixes[1:-1]
    #print(prefixes)
    #print(suffixes)
    if len(prefixes)!=0:
        for i in range(1,len(prefixes)+1):
            if prefixes[-i] in suffixes:
                found=True
                print(word+word[len(prefixes[-i]):])
                break
        if not found:
            print(word+word)
    else:
        print(word+word)