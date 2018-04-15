import heapq
class Node:
    def __init__(self,data,freq,left,right):
        self.freq=freq
        self.symbol=data
        self.left=left
        self.right=right
        self.edgevalue = -1

    def __lt__(self, other):
        if self.freq < other.freq:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.freq > other.freq:
            return True
        else:
            return False

class Huffmann:
    def huffenc(self,Symbols,Freq):
        n=len(Symbols)
        leaves=list()
        for i in range(n):
            leaf = Node(Symbols[i],Freq[i],None,None)
            heapq.heappush(leaves,leaf)

        while len(leaves)!=1:
            x1 = heapq.heappop(leaves)
            x2 = heapq.heappop(leaves)
            node = Node("*",x1.freq+x2.freq,x1,x2)
            heapq.heappush(leaves,node)


        return heapq.heappop(leaves)

    def encodedValues(self, root,b):
        if root.left  != None:
            b = b + "0"
            self.encodedValues(root.left,b)
        if root.symbol !="*":
            print("value of " + root.symbol + "  is = " + b)
            b=""
        else :
            newstring=""
            for i in range(len(b)-1):
                newstring+=b[i]
            b=newstring
        if root.right !=None:
            b= b +"1"
            self.encodedValues(root.right,b)

    def traverse(self,root):
        current_level = [root]
        while current_level:
            print(' '.join(str(node.freq) for node in current_level))
            next_level = list()
            for n in current_level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
                current_level = next_level





Symbols = ['a','b','c','d','e','f']
Freq = [20,12,10,8,4,3]
h = Huffmann()
h.traverse(h.huffenc(Symbols,Freq))
b=""
h.encodedValues(h.huffenc(Symbols,Freq),b)









