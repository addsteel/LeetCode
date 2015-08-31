import Queue
class Stack:
    # initialize your data structure here.
	def __init__(self):
		self.inQueue = Queue.Queue(0)
		self.outQueue = Queue.Queue(0)
	# @param x, an integer
	# @return nothing
	def push(self, x):
		self.inQueue.put(x)
	# @return nothing
	def pop(self):
		self.top()
		if self.outQueue.empty() == False:
			self.outQueue.get()
	# @return an integer
	def top(self):
		if self.outQueue.empty() == False:
			return self.outQueue.get()
		elif self.inQueue.empty() == False:
			myArray = [0 for i in xrange(0,self.inQueue.qsize())]
			for i in xrange(0, len(myArray)):
				myArray[-i-1] = self.inQueue.get()
			for i in xrange(0, len(myArray)):
				self.outQueue.put(myArray[i])
			return self.outQueue.get()
		else:
			return 0
    # @return an boolean
	def empty(self):
		return self.outQueue.empty() and self.inQueue.empty()
s = Stack()
s.push(1)
print s.top()
s.pop()
if s.empty(): print 'EOFError'