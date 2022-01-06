import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))

import time
moths=[31,28,31,30,31,30,31,31,30,31,30,31]
S=readint()
day,hours=readline().split()
year,month,day=[int(x) for x in day.split('/')]
hours,mini,sec=hours.split(':')
hours=int(hours)
what=(hours-S)%24
day += ((hours - S)-(what))//24
hours = (hours - S)%24
countr=month-2
while(True):
    if day<=0:
        day +=moths[countr%12]
        if month==1:
            year-=1
            month=12
        else:
            month-=1
        countr-=1
    else:
        break
print(f"{year}/{str(month).zfill(2)}/{str(day).zfill(2)} {str(hours).zfill(2)}:{mini}:{sec}")