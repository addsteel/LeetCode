class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
	def searchMatrix(self, matrix, target):
		colLength = len(matrix)
		if colLength == 0:	return False
		rowLength = len(matrix[0])
		if rowLength == 0:	return False
		leftElem = [matrix[i][0] for i in range(0,len(matrix))]
		rightElem = [matrix[i][-1] for i in range(0,len(matrix))]
		leftIndex = self.binSearch(leftElem, target)+1
		rightIndex = self.binSearch(rightElem, target)
		if leftIndex == 0 or rightIndex == len(matrix) - 1:
			if target != matrix[-1][-1] and target != matrix[0][0]:
				return False
			else:	return True
		if leftIndex < rightIndex:	return False
		if rightIndex >= 0 and matrix[rightIndex] == target:	return True
		for i in xrange(rightIndex, leftIndex):
			index = self.binSearch(matrix[i], target)
			if index >= 0 and matrix[i][index] == target:	return True
		return False
	#return the index of target in vector. If no, return the index of largest element smaller than
	#target b. If no, return -1
	def binSearch(self, vector, target):
		left = 0
		right = len(vector)
		if right < 1:	return 0
		while left < right:
			mid = (left + right) / 2
			if vector[mid] == target:
				return mid
			elif vector[mid] > target:
				right = mid - 1
			else:
				left = mid + 1
		if left >= len(vector):
			return len(vector) - 1
		if vector[left] > target:	return left - 1
		else:	return left
so = Solution()
matrix = [ [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 14, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
#matrix = [[1,]]
if so.searchMatrix(matrix, 30): print 'In'