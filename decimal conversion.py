# converting a decimal number to any digit

class Stack:
	def __init__(self):
		self.items=[]

	def push(self,cargo):
		self.items.append(cargo)

	def pop(self):
		return self.items.pop()

	def isEmpty(self):
		return self.items==[]

def decimalConverter(number,system):
	S=Stack()
	while(number>0):
		S.push(number%system)
		number=number/system
	while not S.isEmpty():
		print digits[S.items.pop()]




digits="0123456789ABCDE"


decimalConverter(25,8)