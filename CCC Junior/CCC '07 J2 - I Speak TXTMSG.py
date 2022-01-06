import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))

things = {'CU': 'see you', ':-)': "I'm happy", ':-(': "I'm unhappy", ';-)': 'wink', ':-p': 'stick out my tongue', '(~.~)': 'sleepy', 'TA': 'totally awesome', 'CCC': 'Canadian Computing Competition', 'CUZ': 'because', 'TY': 'thank-you', "YW": "you're welcome", 'TTYL': 'talk to you later'}
while(True):
    word=readline()
    if word=='TTYL':
        raise SystemExit(print('talk to you later'))
    try:
        print(things[word])
    except:
        print(word)
        