sentence = input()
vowels = ['a','e','i','o','u']
for x in range(len(sentence)):
    try:
        if sentence[x]=='p' and sentence[x-1] in vowels and sentence[x+1] in vowels:
            sentence=sentence[:x] + sentence[x+2:]
    except(IndexError):
        pass
print(sentence)
