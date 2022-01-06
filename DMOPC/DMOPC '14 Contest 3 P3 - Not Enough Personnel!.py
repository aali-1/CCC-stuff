import sys
input = sys.stdin.readline
N=int(input())
p={}
for _ in range(N):
    name,num=input().split()
    try:
        p[int(num)]
    except(ValueError,KeyError):
        p[int(num)]=name
for _ in range(int(input())):
    one,d=[int(x) for x in input().split()]
    t=dict(map(lambda x: (x[0], x[1]) if x[0] <= one+d and x[0]>=one else (-10000, -10000), p.items())) #sort based on whether the item in the dict is a suitable solution
    kee = lambda k : abs(k - one)
    
    l=list(t.keys())
    
    what = min(l,key=kee)
    if what==-10000:
        print('No suitable teacher!')
    else:
        print(t[what])

'''
5
Kanie 1000
Moffle 929
Sento 950
Macaron 550
Tirami 500
3
930 20
400 150
790 15
'''