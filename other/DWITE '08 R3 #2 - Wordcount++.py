import sys
for _ in range(5):
    words = sys.stdin.readline().split()
    for x in words:
        if "'" in x:
            idex = x.find("'")
            words.append(x[:idex])
            words.append(x[idex+1:])
            words.remove(x)
    wcount=0
    for x in words:
        ccount=0
        for y in x:
            if y.isalpha():
                ccount+=1
        if ccount>3:
            wcount+=1
    print(wcount)