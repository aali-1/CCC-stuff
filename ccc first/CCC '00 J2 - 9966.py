first=int(input())
second=int(input())
interval=list(range(first,second+1))
def canbeflipped(x):
    z=[int(y) for y in str(x)]
    if any(a in z for a in [2,3,4,5,7]):
        return False
    dictionary = {'0':'0', '6':'9', '9': '6', '1' :'1', '8': '8'}
    flipped=''
    for h in str(x)[::-1]:
        flipped += dictionary[h]
    if int(flipped) == int(x):
        return True
    return False
count=0
for x in interval:
    if canbeflipped(x)==True:
        count+=1
print(count)
