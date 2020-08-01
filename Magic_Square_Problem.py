def permutations(ax):
    output = []

    def swap(arr, i_pos, f_pos):
        arr[i_pos], arr[f_pos] = arr[f_pos], arr[i_pos]
        return arr

    def generate(l, arr):
        if l == 1:
            output.append(arr.copy())
            return

        generate(l - 1, arr)
        i = 0
        for i in range(l - 1):
            if l % 2 == 0:
                arr = swap(arr, i, l - 1)
            else:
                arr = swap(arr, 0, l - 1)
            generate(l - 1, arr)

    generate(len(ax), ax)
    return output


def matrix(odd, even):
    if checkMagic([[even[0], odd[0], even[1]], [odd[1], 5, odd[2]], [even[2], odd[3], even[3]]]):
        return [[even[0], odd[0], even[1]], [odd[1], 5, odd[2]], [even[2], odd[3], even[3]]]
    else:
        return False


def checkMagic(ar):
    print(ar)
    for item in ar:
        if sum(item) != 15:
            return False
    for j in range(3):
        su = 0
        for k in range(3):
            su = su + ar[k][j]
        if su != 15:
            return False

    su = 0
    for j in range(3):
        for k in range(3):
            if j == k:
                su = su + ar[j][k]
    if su != 15:
        return False
    su = 0
    for j in range(3):
        for k in range(3):
            if abs(j - k) == 2 or j == k == 1:
                su = su + ar[j][k]
    if su != 15:
        return False
    return True


def calc(ar1, ar2):
    sm = 0
    for i in range(len(ar1)):
        for j in range(len(ar1)):
            sm = sm + abs(ar1[i][j] - ar2[i][j])

    return sm


def formingMagicSquare(s):
    even = permutations([2, 4, 6, 8])
    odd = permutations([1, 3, 7, 9])
    MagicSquares = []
    for item1 in even:
        for item2 in odd:
            crr = matrix(item2, item1)
            if crr:
                MagicSquares.append(crr)

    current = 1000
    for it in MagicSquares:
        exp = calc(s, it)
        if exp < current:
            current = exp
    return current


formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]])
