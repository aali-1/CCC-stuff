def possible_child(m,f,pbaby):
    yes=0
    for x in range(5):
        if pbaby[x] == pbaby[x].lower():
            if pbaby[x] in m[x] and pbaby[x] in f[x]:
                yes+=1
        else:
            if pbaby[x] in m[x] or pbaby[x] in f[x]:
                yes+=1
    if yes==5:
        return True
    return False

m = input()
f = input()
m = [m[i:i+2] for i in range(0, len(m), 2)]
f = [f[i:i+2] for i in range(0, len(f), 2)]
for _ in range(int(input())):
    pbaby = input()
    yes=0
    if possible_child(m,f,pbaby):
        print('Possible baby.')
    else:
        print('Not their baby!')
'''
AABbCcddEe
AaBBccddee
2
ABcDe
ABCdE
aBcdE
ABcdE
ABCde

'''