import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
nums=[]
for i in range(63):
    nums.append(2**i)
#print(nums)
for _ in range(readint()):
    if readint() in nums:
        print('T')
    else:
        print('F')