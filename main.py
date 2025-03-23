def maxssubarraysum(a,asize):
    max=-99999999
    cmax=0
    #add current element to current max,,check if cmax>max,if yes update max,if cmax is less than zero update it to zero
    for i in range(0,asize):
        cmax=cmax+a[i]
        if cmax>0:
            max=cmax
        if cmax<0:
            cmax=0
    return max
a=[1,2,3,4,-5,-3,-5,9,-6,12,-8]
print(maxssubarraysum(a,len(a)))