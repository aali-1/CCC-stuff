num=int(input())
#line one
if num in [0,2,3,5,6,7,8,9]:
    print(" * * *")
else:
    print()
#line two-four
if num in [0,4,8,9]:
    print("*     *")
    print("*     *")
    print("*     *")
elif num in [1,2,3,7]:
    print("      *")
    print("      *")
    print("      *")
else:
    print("*")
    print("*")
    print("*")
#line 5
if num in [2,3,4,5,6,8,9]:
    print(" * * *")
else:
    print()
#line 6-8
if num in [0,6,8]:
    print("*     *")
    print("*     *")
    print("*     *")
elif num in [1,3,4,5,7,9]:
    print("      *")
    print("      *")
    print("      *")
else:
    print("*")
    print("*")
    print("*")
if num in [0,2,3,5,6,8,9]:
    print(" * * *")
else:
    print()
