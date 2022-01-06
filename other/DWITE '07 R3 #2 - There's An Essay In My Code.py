import sys
input = sys.stdin.readline
for _ in range(5):
    line = input()[:-1]
    ans=[]
    for i in range(len(line)):
        try:
            if line[i]=='/' and line[i+1]=='/':
                #print(line[i+2:])
                ans.append(line[i+2:])
                break
            if line[i]=='"':
                #print(i)
                if line.count('"')>1:
                    second = line.find('"', line.find('"') + 1)
                    ans.append(line[i+1:second])
                    line = line[:i] + ' ' + line[second + 1:]
                    #print(line)
            if line[i]=="'":
                #print(i)
                if line.count("'")>1:
                    second = line.find("'", line.find("'") + 1)
                    ans.append(line[i+1:second])
                    line = line[:i] + ' ' + line[second + 1:]
                    #print(line)
            if line[i]=='/' and line[i+1]=='*':
                if '*/' in line:
                    for y in range(len(line[i:])):
                        if line[y]=='*' and line[y+1]=='/':
                            thing=y
                    ans.append(line[i+2:thing])
                    line=line[:i+1]+' '+line[thing+2:]
        except(IndexError):
            pass
    #print(ans)
    print(*ans,sep=' ')