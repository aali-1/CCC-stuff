import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for x in range(n)]
print(min(sum(a)-max(a),int(sum(a)/2)))