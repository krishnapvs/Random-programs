# Largest Sum Contiguous Subarray
#Write an efficient python program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.

def largestSumContiguousSubArray(A):
	max_so_far=max_end_here=0
	for i in A:
		max_end_here=max_end_here+i
		if max_end_here<0:
			max_end_here=0
		if max_end_here>max_so_far:
			max_so_far=max_end_here
	print max_so_far
	return

A=[int(i) for i in (raw_input("Enter your input: ")).split()]
largestSumContiguousSubArray(A)
print A
