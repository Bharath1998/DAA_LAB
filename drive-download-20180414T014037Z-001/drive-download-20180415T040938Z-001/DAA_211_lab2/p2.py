def search(a,l,h):
    mid=(l+h)//2
    if a[mid] > a[mid-1] and a[mid] < a[mid+1]:
        search(a,mid+1,len(a)-1)
    elif a[mid] > a[mid-1] and a[mid] > a[mid+1]:
        return a[mid]
    else:
        print("holla")

print("enter the number of elements")
s=int(input())
h=list()
print("enter the elements")
for i in range(s):
    h.append(int(input()))

x=search(h,0,len(h)-1)

print(x)