check=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
time = {'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 3, 'g': 1, 
'h': 2, 'i': 3, 'j': 1, 'k': 2, 'l': 3, 'm': 1, 'n': 2, 'o': 3, 
'p': 1, 'q': 2, 'r': 3, 's': 4, 't': 1, 'u': 2, 'v': 3, 'w': 1, 
'x': 2, 'y': 3, 'z': 4}
while(True):
    totaltime=0
    word=input()
    
    if word=='halt':
        break
    for c in range(len(word)):
        try:
            button = [s for s in check if word[c] in s]
            otherbutton = [s for s in check if word[c+1] in s]
            if button==otherbutton:
                totaltime+=2
        except(IndexError):
            pass
        totaltime+=time[word[c]]
    print(totaltime)
