import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    found = False
    one,two,three = input()[:-1],input()[:-1],input()[:-1]
    words=[one,two,three]
    for x in words:
        new = words.copy()
        new.remove(x)
        if any(word.startswith(x) for word in new) or any(word.endswith(x) for word in new):
            found = True
            print('No')
            break
    if not found:
        print('Yes')
'''
1
a
ab
aa
'''