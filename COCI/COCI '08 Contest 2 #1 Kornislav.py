#greedy algorithm: highest steps forward, turn minimum, turn second highest, turn whatevers left
import sys
input = sys.stdin.readline
all = [int(x) for x in input().split()]
all.sort()
print(all[-2]*all[0])