import sys
class Marshall():
    def __init__(self,n):
        self.matrix = [[[sys.maxsize for i in range(n)] for j in range(n)] for k in range(n)]
        self.pi = [[[-1 for i in range(n)] for j in range(n)] for k in range(n)]
        # dist = [[100 for i in range(n)]]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i==j:
                        self.matrix[k][i][j]=0
                        self.pi[k][i][j] = i+1


    def FloydWarshal(self,n):


        for k in range(1,n):
            for i in range(n):
                for j in range(n):
                    if(self.matrix[k-1][i][j]<=(self.matrix[k-1][i][k]+self.matrix[k-1][k][j])):
                        self.pi[k][i][j] = self.pi[k-1][i][j]
                    else:
                        self.pi[k][i][j] = self.pi[k-1][k][j]

                    self.matrix[k][i][j]=min(self.matrix[k-1][i][j],self.matrix[k-1][i][k]+self.matrix[k-1][k][j])


        return self.matrix[n-1]

def main():
    print("Enter the number of vertices")
    n = int(input())
    Fly = Marshall(n)
    print("Enter the number of edges")
    e = int(input())
    print("Enter the directed edges , source to destination and weight")
    for i in range(e):
        u,v,w = map(int,input().split())
        Fly.matrix[0][u-1][v-1]=w
        Fly.pi[0][u-1][v-1]=u
    ans = Fly.FloydWarshal(n)
    for i in range(len(ans)):
        for j in range(len(ans)):
            if ans[i][j]!=sys.maxsize and sys.maxsize - ans[i][j]>=1000:
                print(ans[i][j], end="    ")
            else:
                print("--", end="    ")
        print()

    print("*******************************************************************")
    for i in range(len((Fly.pi[n-1]))):
        for j in range(len(Fly.pi[n-1])):
            print(Fly.pi[n-1][i][j], end="    ")
        print()

if __name__=='__main__':
    main()