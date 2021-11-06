import sys
for _ in range(5):
    line = sys.stdin.readline()
    if any(x in line for x in ['(',')','[',']','{','}']):
        stack=[]
        ub=False
        for x in line:
            if x == '(':
                stack.append(')')
            if x == '[':
                stack.append(']')
            if x == '{':
                stack.append('}')
            if x==')' or x ==']' or x=='}':
                try:
                    if stack[-1]!=x:
                        ub=True
                except(IndexError):
                    ub=True
                if not ub:
                    stack.pop()
        
        print('not balanced') if ub or len(stack)>0 else print('balanced')
    else:
        print("balanced")