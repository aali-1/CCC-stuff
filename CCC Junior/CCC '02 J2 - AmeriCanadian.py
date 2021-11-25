while True:
    word = input()
    if word=='quit!':
        break
    if word[-2:]=='or' and len(word)>4 and word[-3] not in ['a','e','i','o','u']:
        word=word[:-1]+"u"+word[-1:]
    print(word)