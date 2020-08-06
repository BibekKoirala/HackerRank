def search(arr,start,end,i):
    if start+1 != end:
        print('start',start)
        print('end',end)
        mid = int((start+end)/2)
        if i>arr[mid]:
            return search(arr,start,mid,i)
        else:
            return search(arr,mid+1,end,i)
    else:
        st = start
        return st+2



print(search([100,70, 50, 40, 20, 10],0,5,60))
def climbingLeaderboard(scores, alice):
    output = []
    score = {}
    for i in scores:
        if i not in score:
            score[i] = 1

    print(score.keys())

    for sc in alice:
        i = 1
        for s in score:
            if sc >= s:
                output.append(i)
                break
            if i == len(score) and sc <= s:
                output.append(i+1)
                break
            i += 1

    print(output)

    return output


#climbingLeaderboard([100, 100, 50, 40, 40, 20, 10],[5, 25, 50, 120])