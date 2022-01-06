import sys
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
gi = lambda: list(map(int, readline().split()))
N,M=gi()
count=0
def findPairs(arr, N, M):
    left,right,result =0, N-1,0
    while (left < right):
        if (arr[left] + arr[right] <= M):
            result += (right - left)
            left += 1
        else:
            right -= 1
    return result
ls = sorted(gi())
print(findPairs(ls, N, M))