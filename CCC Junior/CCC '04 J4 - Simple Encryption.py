letters={'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 
7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 
'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 
'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
valuez = list(letters.values())
keyz=list(letters.keys())
keyword = input()
length = len(keyword)
bigmsg = ''.join((filter(str.isalpha, input()))).upper()
encrypted=[]
for x in range(len(bigmsg)):
    index=x%length
    keyletternum=letters[keyword[index]]-1
    keyenc=letters[bigmsg[x]]
    try:
        newletter=valuez.index((keyenc+keyletternum)%26)
        print(keyz[newletter],end="")
    except(KeyError, ValueError):
        #print("\n",keyenc,keyletternum,bigmsg[x],keyword[index])
        print("Z",end="")
    

