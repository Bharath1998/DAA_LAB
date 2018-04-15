def solvehanoi(n,s,i,t):
    if n > 1:
        solvehanoi(n-1,s,t,i)
        print("Move Disc "+ str(n) + "from peg "+ str(s) +"to peg  "+str(t))
        solvehanoi(n-1,i,s,t)
    elif n==1:
        print("move disc "+str(n)+" from peg "+ str(s) +"to peg  "+str(t))
print("enter the number of disks")
a=int(input())
solvehanoi(a,'s','i','t')