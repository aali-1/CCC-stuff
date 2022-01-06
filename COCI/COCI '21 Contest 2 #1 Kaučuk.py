import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
N = readint()
sec=0
subsec=0
subsubsec=0
for _ in range(N):
  word,name=readline().split()
  if word=='section':
    sec+=1
    subsec=0
    subsubsec=0
    print(sec,name)
  elif word=='subsection':
    subsubsec=0
    subsec+=1
    print(sec,'.',subsec,' ',name,sep='')
  else:
    subsubsec+=1
    print(sec,'.',subsec,'.',subsubsec,' ',name,sep='')
