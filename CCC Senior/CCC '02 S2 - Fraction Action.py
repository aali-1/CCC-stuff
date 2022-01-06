import sys
from math import gcd
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
nume=readint()
deno=readint()
if nume%deno==0:
    print(nume//deno)
else:
    gdc=gcd(nume,deno)
    if nume>deno:
        print(nume//deno,f"{(nume%deno)//gdc}/{deno//gdc}")
    else:
        print(f"{nume//gdc}/{deno//gdc}")
    