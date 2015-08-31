from collections import defaultdict
class Solution:
	def __init__(self):
		self.path = set()
		self.visited = set()
		self.vex = defaultdict(list)
	# @param {integer} numCourses
	# @param {integer[][]} prerequisites
	# @return {boolean}
	def canFinish(self, numCourses, prerequisites):
		if numCourses == 0 or prerequisites == []:
			return True
		length = numCourses
		inDegree = [0 for i in xrange(0, length)]
		for pair in prerequisites:
			self.vex[pair[0]].append(pair[1])
			inDegree[pair[1]] += 1
		index = 0
		while index < length:
			if inDegree[index] != 0 and index not in self.visited and self.depthFirstTrace(index) == True:	return False
			index += 1
		return True
	def depthFirstTrace(self,node):
		if node in self.path:	return True
		else:
			self.path.add(node)
			for v in self.vex[node]:
				if v not in self.visited and self.depthFirstTrace(v) == True:
					return True
			self.path.remove(node)
			self.visited.add(node)
			return False
		return False
so = Solution()
numCourses = 3
prerequisites = []
prerequisites.append([0,1])
prerequisites.append([0,2])
prerequisites.append([1,2])
if so.canFinish(numCourses, prerequisites):
	print 'Can'