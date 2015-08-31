class Solution:
	def __init__(self):
		self.board = []
		self.tracTable = []
		self.xSize = 0
		self.ySize = 0
	# @param {character[][]} board
	# @param {string[]} words
	# @return {string[]}
	def findWords(self, board, words):
		self.board = board
		self.xSize = len(board)
		if self.xSize > 0:
			self.ySize = len(board[0])
		self.tracTable = [[True for i in xrange(0,self.ySize)] for j in xrange(0, self.xSize)]
		result = []
		for word in words:
			if self.exist(word):
				result.append(word)
		return result
	# @param {character[][]} board
	# @param {string} word
	# @return {boolean}
	def exist(self, word):
		if len(word) == 0:	return True
		#self.xSize = len(board)
		#if self.xSize > 0:
			#self.ySize = len(board[0])
		#self.tracTable = [[True for i in xrange(0,self.ySize)] for j in xrange(0, self.xSize)]
		#print self.xSize, self.ySize
		#print board[0], len(board[0])
		#str = "abc"
		#print len(str)
		if len(word) > self.xSize * self.ySize:	return False
		for i in xrange(0, self.xSize):
			for j in xrange(0, self.ySize):
				if self.board[i][j] == word[0]:
					self.tracTable[i][j] = False
					if self.trace(word[1:], i, j) == True:
						self.tracTable[i][j] = True
						return True
					self.tracTable[i][j] = True
		return False
	def trace(self, word, x, y):
		if self.tracTable[x][y] != False:	return False
		if len(word) == 0:	return True
		if len(word) < 0:	return False
		if x + 1 < self.xSize:
			if self.tracTable[x+1][y] and self.board[x+1][y] == word[0]:
				self.tracTable[x+1][y] = False
				if self.trace(word[1:], x+1, y) == True:
					self.tracTable[x+1][y] = True
					return True
				self.tracTable[x+1][y] = True
		if y + 1 < self.ySize:
			if self.tracTable[x][y+1] and self.board[x][y+1] == word[0]:
				self.tracTable[x][y+1] = False
				if self.trace(word[1:], x, y+1) == True:
					self.tracTable[x][y+1] = True
					return True
				self.tracTable[x][y+1] = True
		if x - 1 >= 0:
			if self.tracTable[x-1][y] and self.board[x-1][y] == word[0]:
				self.tracTable[x-1][y] = False
				if self.trace(word[1:], x-1, y) == True:
					self.tracTable[x-1][y] = True
					return True
				self.tracTable[x-1][y] = True
		if y - 1 >= 0:
			if self.tracTable[x][y-1] and self.board[x][y-1] == word[0]:
				self.tracTable[x][y-1] = False
				if self.trace(word[1:], x, y-1) == True:
					self.tracTable[x][y-1] = True
					return True
				self.tracTable[x][y-1] = True
		return False
#board = [ "AAAA", "AAAA", "AAAB" ]
board = ["AAAAB"]
so = Solution()
if so.exist(board, "AB"):
	print 'True'
else:
	print 'False'