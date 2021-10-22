for x in range(int(input())):
    a=int(input())
    while a>9:
        a=eval(str(tuple(list(map(int, str(a))))).replace(',','+'))
    print(a)