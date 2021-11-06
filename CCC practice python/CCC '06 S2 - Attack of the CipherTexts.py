letters={'A': '.', 'B': '.', 'C': '.', 'D': '.', 'E': '.', 'F': '.', 'G': 
'.', 'H': '.', 'I': '.', 'J': '.', 'K': '.', 'L': '.', 'M': '.', 'N': '.', 
'O': '.', 'P': '.', 'Q': '.', 'R': '.', 'S': '.', 'T': '.', 'U': '.', 
'V': '.', 'W': '.', 'X': '.', 'Y': '.', 'Z': '.', ' ':'.'}
plain = input()
enc = input()
other = input()
for x in range(len(plain)):
    letters[enc[x]]=plain[x]
for x in range(len(other)):
    print(letters[other[x]],end="")