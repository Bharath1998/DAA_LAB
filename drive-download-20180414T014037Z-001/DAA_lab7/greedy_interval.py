def resources(intervals):
    temp = list()
    f = 0
    g=0
    temp.append(intervals[0])
    for i in range(1, len(intervals)):
        if (temp[f][0] < intervals[i][0] and temp[f][1] < intervals[i][0]):
            temp.append(intervals[i])
            intervals[i]=[0,0]
            f = f + 1
        if intervals[i]==[0,0]:
            g=g+1
    print(temp)
    if g==len(intervals):
        resources(intervals)




print("Enter the number of intervals")
n = (int)(input())
print("enter the intervals")
intervals = list()
for i in range(n):
        u,v=map(int,input().split())
        intervals.append([u,v])

intervals=sorted(intervals,key=lambda item:item[1])
resources(intervals)