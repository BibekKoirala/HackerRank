def check(st):
    i = 0
    j = 1
    k = 2
    if len(st) == 1:
        return 'NO'
    if len(st) == 2:
        if int(st[1]) - int(st[0]) == 1:
            return 'YES ' + st[0]
        else:
            return 'NO'

    a = st[i:j]
    b = st[j:k]
    while k < len(st) + 1:
        if (int(b) - int(a)) == 1:
            break
        k += 1
        a = st[i:j]
        b = st[j:k]
        if (int(b) - int(a)) == 1:
            break
        j += 1
        k += 1
        a = st[i:j]
        b = st[j:k]
    print('this is b',b)
    x = len(b)
    print('x',x)
    m = k + k - j
    a = st[j:k]
    b = st[k:m]

    print(x)
    print(len(st)//2)
    if x == (len(st)/2):
        return 'YESsss'
    while m < len(st) + 1:
        print(int(a) - int(b))
        if int(b) - int(a) != 1:
            return 'NO'
        j = j + x
        k = k + x
        m = m + x
        a = st[j:k]
        b = st[k:m]

    return 'Yes'


def separateNumbers(s):
    output = []
    for i in s:
        print(check(i))


separateNumbers(['91', '1213'])
