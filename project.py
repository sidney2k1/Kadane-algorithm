def longestevenoddsubarray(arr,n):
    longest=1
    cnt=1
    for i in range(n-1):
        if (arr[i]+arr[i+1])%2==1:
            cnt=cnt+1
        else:
            longest=max(longest,cnt)
            cnt=1
    if longest==1:
        return longest
    return max(cnt,longest)
arr=[1,2,3,4,5,5,4,3,2,1,2,3,3,7,8,77,7,9]
n=len(arr)
print(longestevenoddsubarray(arr,n))