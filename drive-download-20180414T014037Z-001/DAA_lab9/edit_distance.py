def edit_distace(s1,s2,l1,l2):
    dp = [[0 for x in range(l2+1)] for v in range(l1+1)]
    operations = list()
    str=""
    for i in range(l1+1):
        for j in range(l2+1):
            if i==0:
                dp[i][j] = j
            elif j==0:
                dp[i][j] = i
            elif s1[i-1]==s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                if dp[i][j-1] <dp[i-1][j] and dp[i][j-1] < dp[i-1][j-1]:
                    f=1
                if dp[i-1][j] < dp[i][j-1] and dp[i-1][j] < dp[i - 1][j - 1]:
                    f = 2
                if dp[i-1][j-1] <dp[i-1][j] and dp[i-1][j-1] < dp[i][j-1]:
                    f=3
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])
                if f==1:
                    str = str + "insert" + s2[i][j]
                    operations.append(str)
                    str=""
                if f==2:
                    str = str + "remove" + s1[i][j]
                    operations.append(str)
                    str=""
                if f==3:
                    str = str + "replace" + s1[i][j] +"with " +  s2[i][j]
                    operations.append(str)
                    str=""


    return dp[l1][l2]


str1 = "sunday"
str2 = "saturday"

print(edit_distace(str1, str2, len(str1), len(str2)))