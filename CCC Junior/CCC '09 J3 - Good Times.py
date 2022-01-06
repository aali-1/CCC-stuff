import sys
input = sys.stdin.readline
n=int(input())
print(n,'in Ottawa')
print((n-300)%2400,'in Victoria')
print((n-200)%2400,'in Edmonton')
print((n-100)%2400,'in Winnipeg')
print(n,'in Toronto')
print((n+100)%2400,'in Halifax')
last = n%10
n+=100
if len(str(n))>1:
    slast=(n//10)%10
    combined=(int(str(slast)+str(last))+30)%60
    #print(combined)
    if combined<abs(n)%100:
        n+=100
        print((str(int(str(n)[:-2])%24))+str(combined),"in St. John's")
    else:
        print((str(int(str(n)[:-2])%24))+str(combined),"in St. John's")
else:
    print(n+30,"in St. John's")