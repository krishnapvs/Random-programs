# Reverses and returns a new array with reversed elements

def reverse_recursive(A):
	if len(A)==1:
		B=[]
	else:
		B=reverse_recursive(A[1:])
	B.append(A[0])
	return B

def reverse_iterative(A):
	B=list(A)
	j=len(A)-1
	for i in range(len(A)/2):
		
		print i,j
		if i==j:
			return B
		else:
			temp=B[i]
			B[i]=B[j]
			B[j]=temp
			j-=1

#test

A=[1,2,3,4,5,6,7,8,99,99]
print 'A',A
print reverse_recursive(A)
print reverse_iterative(A)
