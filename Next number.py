
number=raw_input("Enter the number: ")
l=[]
for i in number:
	l.append(i)
a=list(l)

a.sort()
a.reverse()


if (a==l):
	print "there is no next big number"
	exit()
A=[]
l.reverse()
#print l
for i in l:
	A.append(int (i))

for i in range(len(l)):
	if A[i]<A[i-1]:
		break
print A[i],A[i-1]
temp=0
for j in range(1,i-1):
	if A[temp]<=A[i]:
		temp=j

dummy=A[temp]
A[temp]=A[i]
A[i]=dummy
a=A[:i]
a.reverse()
A=a+A[i:]
A.reverse()
total=0	
for i in A:
	total=total*10+i


print total