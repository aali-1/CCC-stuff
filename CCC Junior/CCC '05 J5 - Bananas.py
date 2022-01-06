import sys
import time
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))

def check(word):
    if word=='A':
        return True
    while 'ANA' in word or 'BAS' in word:
        word=word.replace('ANA','A')
        word=word.replace('BAS','A')
        
    if word=='A':
        return True
    return False
        
            


while(True):
    word=readline().upper()
    if word=='X':
        break
    if check(word):
        print('YES')
    else:
        print('NO')
    