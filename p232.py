class Queue:
    # initialize your data structure here.

	def __init__(self):
		self.inStack = []
		self.outStack = []
    # @param x, an integer
    # @return nothing
	def push(self, x):
		self.inStack.append(x)
    # @return nothing
	def pop(self):
		if not len(self.outStack) == 0:	
			self.outStack.pop()
			return 
		while not len(self.inStack) == 0:	self.outStack.append(self.inStack.pop())
		self.outStack.pop()
	# @return an integer
	def peek(self):
		if not len(self.outStack) == 0:	return self.outStack[-1]
		while not len(self.inStack) == 0:
			self.outStack.append(self.inStack.pop())
		return self.outStack[-1]
    # @return an boolean
	def empty(self):
		if len(self.outStack) == 0 and len(self.inStack) == 0:	return True
		else:	return False
#We are fixing our views to another. I rewrite the code and it was accepted.
q = Queue()
for i in range(1,10):
	q.push(i)
for i in range(1,10):
	print q.peek()
	q.pop()
for i in range(1,5):
	q.push(i)
print q.peek()
for i in range(1,5):
	print q.peek()
	q.pop()
if len(q.inStack) == 0 and len(q.outStack) == 0:	print 'Good'