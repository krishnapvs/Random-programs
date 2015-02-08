# Reverses and returns a new array with reversed elements

def reverse(A):
	if len(A)==1:
		B=[]
		b.append(A[0])
		return B
	else:
		B=reverse(A[1:])
		B.append(A[0])


#test

A=[1,2,3,4,5,6,7,8,99,99]
print reverse(A)
