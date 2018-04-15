def mergesort(A,low,high):
    inv_count=0
    if low < high :
         mid = (low+high)//2
         inv_count = mergesort(A,low,mid)
         inv_count = inv_count + mergesort(A,mid+1,high)
         inv_count = inv_count + merge(A,low,mid,high)
    if low==high:
        return 0
    return inv_count
def merge(A,low,mid,high):
    L=A[low:mid+1]
    R=A[mid+1:high+1]
    inv_count=0
    r=0
    l=0
    i=low
    while l<len(L) and r<len(R):
        if L[l]>R[r]:
            A[i]=R[r]
            r=r+1
            inv_count=inv_count+(len(L)-l)
        else:
            A[i]=L[l]
            l=l+1
        i=i+1
    while r<len(R):
        A[i]=R[r]
        r=r+1
        i=i+1
    while l<len(L):
        A[i]=L[l]
        l=l+1
        i=i+1


    return inv_count

k=[1,20,6,4,5,-1]
j = mergesort(k,0,len(k)-1)
print(j)
print(k)