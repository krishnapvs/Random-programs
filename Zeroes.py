# Making rows and columns zeroes
# rows and columns
M=int(raw_input("Enter number of rows: "))
N=int(raw_input("Enter number of columns: "))
matrix=[]
rows=[]
columns=[]
for i in range(M):
	temp=[]
	a=raw_input("Enter a row: ")
	for j in range(N):
		temp.append(int(a[j]))
	matrix.append(temp)

for i in range(M):
	for j in range(N):
		if matrix[i][j]==0:
			rows.append(i)
			columns.append(j)

for i in rows:
	for j in range(N):
		matrix[i][j]=0
for j in columns:
	for i in range(M):
		matrix[i][j]=0

print matrix
