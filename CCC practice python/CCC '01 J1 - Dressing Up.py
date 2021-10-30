a=int(input())
for x in range(a):
    if x < a/2:
        print('*'*(x*2+1)+' '*(2*a-2*(x*2+1))+'*'*(x*2+1))
    if x > a/2:
        print('*'*((a-x)*2-1) +' '*(2*a-(2*(a-x)*2)+2)+'*'*((a-x)*2-1))
