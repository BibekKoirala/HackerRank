def nonDivisibleSubset(k, s):
    # Write your code here
    output = 0
    m = {ct: 0 for ct in range(k)}

    for i in s:
        m[i % k] += 1
    output += min(m[0], 1)
    start = 1
    end = len(m) - 1

    if k % 2 == 0:
        output += min(m[(k // 2)], 1)

    while start < end:
        print(start + end)
        output += max(m[start], m[end])
        start += 1
        end -= 1

    return output


print(nonDivisibleSubset(7,[278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]))

