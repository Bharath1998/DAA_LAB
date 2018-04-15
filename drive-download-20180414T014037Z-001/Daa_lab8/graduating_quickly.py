def count(store,y,sem):
    temp=[]
    f=0
    for i in range(len(y)):
        if y[i]==0:
            y[i]=y[i]-1
            temp.append(i)
            f=1
    for i in range(len(temp)):
        for k in store[temp[i]]:
            y[k]=y[k]-1
    if f==0:
        return sem
    sem+=1
    return count(store,y,sem)


print("enter number of vertices")
n=int(input())
store=[[] for i in range(n)]
y=[0 for i in range(n)]
print("enter the edge combinations")
for i in range(n-1):
    u,v=map(int,input().split())
    store[u].append(v)
print("Adjacency list")
print(store)
for i in range(n):
    for j in store[i]:
        if y[j]==0:
            y[j]=1
        else:
            y[j]=y[j]+1
print("number of inward edges")
print(y)
print("Number of sem")
print(count(store,y,0))
