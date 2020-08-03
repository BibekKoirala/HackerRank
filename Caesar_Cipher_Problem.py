def isCap(a):
    if 64 < ord(a) < 91:
        return True
    return False


def isSml(a):
    if 96 < ord(a) < 123:
        return True
    return False


def caesarCipher(s, k):
    fin = ''
    for i in s:
        if isCap(i):
            asci = ord(i)
            if (asci + k) > 90:
                nk = asci + k - 90
                while nk > 26:
                    nk = nk - 26
                fin = fin + chr(64 + nk)
            else:
                fin = fin + chr(asci + k)
        elif isSml(i):
            asci = ord(i)
            if (asci + k) > 122:
                nk = asci + k - 122
                while nk > 26:
                    nk = nk - 26
                fin = fin + chr(96 + nk)
            else:
                fin = fin + chr(asci + k)
        else:
            fin = fin + i
    print(fin)
    return fin

caesarCipher('www.abc.xy',87)
