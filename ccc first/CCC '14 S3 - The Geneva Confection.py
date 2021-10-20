import sys
cases = int(sys.stdin.readline())
for x in range(cases):
    amount = int(sys.stdin.readline())
    end=[]
    branch=[0]
    cars=[0]
    for _ in range(amount):
        cars.append(int(sys.stdin.readline()))
    required=1
    success=True
    while True:
        if cars[-1]==required:
            del[cars[-1]]
            required+=1
        elif branch[len(branch)-1]==required:
            del[branch[-1]]
            required+=1
        elif len(cars)>1:
            branch.append(cars[-1])
            del[cars[-1]]
        else:
            success=False
            break
        if required-1==amount:
            break
    if success == False:
        print ("N")
    else:
        print ("Y")


'''
1
5
5
2
3
1
4

'''