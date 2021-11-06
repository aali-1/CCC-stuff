import sys
thing=sys.stdin.readline().split()
stack=[]
for x in thing:
    try:
        stack.append(int(x))
    except(ValueError):
        if x=='^':
            x='**'
        last=stack[-1]
        slast=stack[-2]
        stack.pop()
        stack.pop()
        stack.append(f"({slast}{x}{last})")
print(round(float(eval(''.join(list(stack[0])))),1))

