import sys
input = sys.stdin.readline
pink = int(input())
green = int(input())
red = int(input())
orange = int(input())
needed = int(input())
combinations = 0

for x in range(needed//pink+1):
    for y in range(needed//green+1):
        for z in range(needed//red+1):
            for j in range(needed//orange+1):
                #print('hello')
                if (x*pink)+(y*green)+(z*red)+(j*orange)==needed:
                    try:
                        thing = x+y+z+j
                        if minimum<thing:
                            minumum = thing
                    except(NameError):
                        minimum = x+y+z+j
                    combinations +=1
                    print(f"# of PINK is {x} # of GREEN is {y} # of RED is {z} # of ORANGE is {j}")
print(f"Total combinations is {combinations}.")                
print(f"Minimum number of tickets to print is {minimum}.")                
                    
