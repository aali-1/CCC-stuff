import sys
def aoft(h1,h2,w):
    actual = (h1+h2)/2
    return (actual*w)

input = sys.stdin.readline
quads = int(input())
heights = [int(x) for x in input().split()]
widths = [int(x) for x in input().split()]
total=0
for x in range(quads):
    total+=aoft(heights[x],heights[x+1],widths[x])
if total.is_integer():
    print(int(total))
else:
    print(total)
    
'''
7 
1000 1000 1000 1000 1000 1000000 100000000 53565
4503487509234 23498572304985 2349587 654654 6454 4554645646 79869
'''    