# Find permutations of given arrayy

output = []


def swap(arr, i_pos, f_pos):
    arr[i_pos],arr[f_pos] = arr[f_pos], arr[i_pos]
    return arr


def generate(l,arr):
    if l == 1:
        output.append(arr.copy())
        return

    generate(l-1,arr)
    i = 0
    for i in range(l-1):
        if l % 2 == 0:
            arr = swap(arr, i, l-1)
        else:
            arr = swap(arr, 0, l-1)
        generate(l-1, arr)


generate(3,[1,2,3])
print(output)