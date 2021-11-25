while(True):
    thing = input()
    if thing=='99999':
        break
    direction = sum([int(x) for x in (str(thing)[:2])])
    if direction%2==0 and direction!=0:
        proper = 'right'
    elif direction%2==1:
        proper = 'left'
    print(proper,thing[2:5])