def number(men,women,n):
	for i in range(len(men)):
		if n==men[i] or n==women[i]:
			return i
def marriage(m_pref,iwp,men,women):
	m1=[len(men)-i-1 for i in range(len(men))]
	wife=[None for i in range(5)]
	h=[None for i in range(5)]
	c=[0 for i in range(5)]
	while(len(m1)!=0):
		m=m1.pop()
		for i in range(c[m],5):
			w=m_pref[m][c[m]]
			c[m]+=1
			if(h[w]==None):
				wife[m]=w
				h[w]=m
				break
			elif(iwp[w][m]<iwp[w][h[w]]):
				wife[m]=w
				m1.append(h[w])
				h[w]=m
				break
	for i in range(5):
		print(men[i],"with",women[wife[i]])

m_p=[[0]*5]*5
w_p=[[0]*5]*5
lines=[]
with open('input.txt','r') as f:
	men=f.readline().split()
	women=f.readline().split()
	for line in f:
         lines.append(line.strip().split()[1:])
l=len(lines)
for i in range(l//2):
	m_p[i]=[number(men,women,i) for i in lines[i]]
	w_p[i]=[number(men,women,i) for i in lines[l//2+i]]

iwp=[[0 for i in range(len(men))] for i in range(len(women))]
for i in range(5):
	for j in range(5):
		jk=w_p[i][j]
		iwp[i][jk]=j
marriage(m_p,iwp,men,women)


