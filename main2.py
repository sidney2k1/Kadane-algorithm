#standard kadane's algorithm to find maximum subarray sum
def kadane(a):
    n=len(a)
    maxsofar=0
    maxending=0
    for i in range(0,n):
        maxending=maxending+a[i]
        if maxending>maxsofar:
            maxsofar=maxending
        if maxending<0:
            maxending=0
    return maxsofar
#the function returns maximum contiguous sum in a[]
def maxcircularsum(a):
    n=len(a)
    maxkadane=kadane(a)
    maxwrap=0
    for i in range(0,n):
        maxwrap+=a[i]
        a[i]=-a[i]
    maxwrap=maxwrap+kadane(a)
    if maxwrap>maxkadane:
        return maxwrap
    else:
        return maxkadane
a=[-10,-11,20,-12,21,-23,-10,10,5,6,8,9]
print("Maximum circular sum:",maxcircularsum(a))
