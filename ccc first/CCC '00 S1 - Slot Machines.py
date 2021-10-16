a,b,c,d=int(input()),int(input()),int(input()),int(input())
count=0
acount,bcount,ccount=0,0,0
while a>0:
    if count%3==0:
        acount+=1
        if (acount+b)%35==0:
            a+=30
    elif count%3==1:
        bcount+=1
        if (bcount+c)%100==0:
            a+=60
    elif count%3==2:
        ccount+=1
        if (ccount+d)%10==0:
            a+=9
    a-=1
    count+=1
print("Martha plays",count,"times before going broke.")
