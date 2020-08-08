def search(arr,start,end,i):
    if abs(start-end) != 1:
        mid = int((start+end)/2)
        if i > arr[mid]:
            return search(arr,start,mid,i)
        else:
            return search(arr,mid,end,i)
    else:
        if i == arr[start]:
            return end
        return end+1


def climbingLeaderboard(scores, alice):
    output = []
    score = []
    for i in scores:
        if i not in score:
            score.append(i)
    print(score)

    for sc in alice:
        if sc > score[0]:
            output.append(1)
        elif sc < score[len(score)-1]:
            output.append(len(score) + 1)
        else:
            output.append(search(score,0,len(score)-1,sc))

    print(output)

    return output


climbingLeaderboard([100, 100, 50, 40, 40, 20, 10],[5, 25, 50, 120])

