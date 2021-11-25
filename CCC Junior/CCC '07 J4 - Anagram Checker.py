sent1=input().split()
sent2=input().split()
sent1=sorted(''.join(sent1))
sent2=sorted(''.join(sent2))
if sent1==sent2:
    print("Is an anagram.")
else:
    print("Is not an anagram.")
