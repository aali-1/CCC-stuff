valuez = ['','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
keyz = [int(x) for x in input().split()]
nums = {}
for x in range(len(keyz)):
    nums[valuez[keyz[x]-1]]=x+1
word = list(input())
keyz = list(nums.keys())
valuez = list(nums.values())
for i in range(len(word)):
    filterertwo=None
    filterer = list(filter(lambda a: word[i] in a, keyz))[0]
    try:
        filterertwo = list(filter(lambda a: word[i+1] in a, keyz))[0]
    except(IndexError):
        pass
    numclick = nums[filterer]
    for j in range(len(filterer)):
        print(numclick,end='')
        if filterer[j]==word[i] and j!=len(filterer)-1:
            break
    if filterertwo==filterer:
        print('#',end='')
'''
3 9 6 8 7 5 1 4 2
ihb
'''
