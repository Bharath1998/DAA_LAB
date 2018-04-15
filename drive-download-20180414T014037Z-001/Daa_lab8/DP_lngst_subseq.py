def Longest(arr):
    dp=[1 for i in range(len(arr))]
    for i in range(1,len(arr)):
        for j in range(len(arr)):
            if arr[i]>arr[j] and dp[i]<dp[j]+1:
                dp[i]=dp[j]+1

maximum=0
    for i in range(len(arr)):
        maximum=max(dp[i],maximum)

return maximum

arr = [10, 22, 9, 33, 21, 50, 41, 60]
print ("Length of lis is", Longest(arr))
