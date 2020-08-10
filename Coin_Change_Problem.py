def getWays(n, c):
    # Write your code here
    t = filter(lambda x: x <= n, c)
    ar = [1 if i==0 else 0 for i in range(n+1)]

    for i in c:
        j = 1
        while j<=n:
            if j<i:
                j += 1
                continue
            ar[j] = ar[j]+ar[j-i]
            j += 1
    print(ar[n])

getWays(15, [2,3,5,10])