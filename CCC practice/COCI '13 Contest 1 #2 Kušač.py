import sys
from math import lcm
N,M=map(int,sys.stdin.readline().split())
print(int((((lcm(N,M)/N)-1)*N)/(lcm(N,M)/M)))