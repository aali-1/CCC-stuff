import sys
input = sys.stdin.readline
primesj=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
for _ in range(5):
    primes=primesj.copy()
    num=int(input())
    if num in primes:
        first=primes[primes.index(num)-2]
        second=primes[primes.index(num)+2]
    else:
        primes.append(num)
        primes.sort()
        #print(primes)
        first=primes[primes.index(num)-2]
        second=primes[primes.index(num)+2]
    if abs(num-first)>=abs(num-second):
        print(second)
    else:
        print(first)