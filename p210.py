class Solution:
	def __init__(self):
		self.inEdge = []
		self.outEdge = []
	# @param {integer} numCourses
	# @param {integer[][]} prerequisites
	# @return {boolean}
	def findOrder(self, numCourses, prerequisites):
		if prerequisites == []:
			return [i for i in xrange(0, numCourses)]
		length = numCourses
		self.inEdge = [set() for i in xrange(0,length)]
		self.outEdge = [set() for i in xrange(0,length)]
		for pair in prerequisites:
			self.inEdge[pair[0]].add(pair[1])
			self.outEdge[pair[1]].add(pair[0])
		index = 0
		path = []
		visited = [False for i in xrange(0,length)]
		while True:
			while index < length and ( visited[index] == True or len(self.inEdge[index]) != 0):	index += 1
			if index == length:
				index = 0
				while index < length and ( visited[index] == True or len(self.inEdge[index]) != 0 ):	index += 1
				if index == length: break
			path.append(index)
			visited[index] = True
			for node in self.outEdge[index]:
				self.inEdge[node].remove(index)
			index += 1
		for node in xrange(0,length):
			if visited[node] == False:
				if len(self.inEdge[node]) == 0:	path.append(node)
				else:	return []
		if len(path) == length:	return path
		else:	return []
so = Solution()
print so.findOrder(2,[[0,1]])