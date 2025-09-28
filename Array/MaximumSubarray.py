def maxSubArray(arr):
    currentsum = arr[0]
    maxsum = arr[0]
    for i in range(1, len(arr)):
        currentsum = max(arr[i], currentsum + arr[i])
        maxsum = max(maxsum, currentsum)
    return maxsum
    # max_sum=0
    # for i in range (len(arr)):
    #     sum=0
    #     for j in range (i,len(arr)):
    #         sum+=arr[j]
    #         if max_sum < sum:
    #             max_sum=sum
    # return max_sum

print(maxSubArray([4,3,5,1]))