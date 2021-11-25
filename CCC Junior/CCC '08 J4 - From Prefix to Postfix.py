import sys
while(True):
    prefix = sys.stdin.readline().split()
    if prefix[0]=='0':
        sys.exit()
    if len(prefix)==1:
        print(prefix[0])
    else:
        stack=[]
        for c in prefix[::-1]:
            try:
                int(c)
                stack.append(int(c))
            except ValueError:
                if c in ['-','+']:
                    last=stack[-1]
                    slast=stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(f"{last}{slast}{c}")
                    #stack.reverse()
        print(' '.join(list(stack[0])))





'''infix=stack
stack=[]
opstack=[]
infix=list(infix[0])
print(infix)
for k in infix:
    try:
        int(k)
        stack.append(int(k))
    except ValueError:
        if len(opstack)==0:
            opstack.append(k)
        else:
            stack.append(opstack[0])
            opstack.pop()
            opstack.append(k)
    if len(stack)==len(infix)-1 and len(opstack)>1:
        stack.append(opstack[0])
    print('stack',stack,'opstack',opstack)
if len(opstack)>0:
        stack.append(opstack[0])
print(stack)'''
'''
1
+ - 2 + 4 5 - - 6 7 8
0
'''