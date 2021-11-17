import sys
sq = 1
snl = {9:34,40:64,54:19,67:86,90:48,99:77}
keyz = list(snl.keys())
while (True):
    roll = int(sys.stdin.readline())
    if roll ==0:
        print('You Quit!')
        break
    sq+=roll
    if sq in keyz:
        sq=snl[sq]
    if sq>100:
        sq-=roll
    print(f"You are now on square {sq}")
    if sq==100:
        print('You Win!')
        break