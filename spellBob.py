for _ in range(int(input())):
    a = list(input())
    b = list(input())
    combi = ['bbo', 'bob', 'obb']
    if a in combi or b in combi:
        print('yes')
    else:
        condition = (('o' in (a[0], b[0]) and 'b' in (a[1], b[1]) and 'b' in (a[2], b[2])) or ('b' in (a[0], b[0]) and 'b' in (a[1], b[1]) and 'o' in (a[2], b[2])) or ('b' in (a[0], b[0]) and 'o' in (a[1], b[1]) and 'b' in (a[2], b[2])))
        print('yes') if condition == True else print('no')
