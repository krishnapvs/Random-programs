# Number of primes till N
import math
n=int(raw_input("Enter a number: "))

for i in range(2,n):
	flag=False
	root=int(math.sqrt(i))
	for j in range(2,root):
		if i%j==0:
			flag=True
			break
	if flag==False:
		print i
if n>2:
	print 2
