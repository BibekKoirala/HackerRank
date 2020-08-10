def Problem(n,m,k):
    arr = [[0 for i in range(len(n)+1)] for j in range(len(m)+1)]

    i = 1
    while i <= len(m):
        j = 1
        while j <= len(n):
            if n[j-1] == m[i-1]:
                arr[i][j] = arr[i-1][j-1] + 1
                j += 1
            else:
                if i >= j and k > 0:
                    n = n[0:i-1]+m[j-1]+n[i:]
                    print(n)
                    k -= 1
                    print(n)
                else:
                    arr[i][j] = max(arr[i][j-1],arr[i-1][j])
                    j += 1
        i += 1
    print(arr)


Problem('abcef','acdef',1)


