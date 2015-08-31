class Solution:
    # @param {string} s
    # @return {string}
	def shortestPalindrome(self, s):
		length = len(s)
		if length <= 1:	return s
		shrinkS = []
		oldChar = s[0]
		i = 0
		while i < length:
			repTime = 0
			while i < length and oldChar == s[i]:
				i += 1
				repTime += 1
			shrinkS.append((oldChar,repTime))
			if i < length: oldChar = s[i]
		leftIndex = 0
		rightPos = len(shrinkS)
		if rightPos == 1:	return s
		while rightPos > 0:
			rightPos -= 1
			leftIndex = 0
			rightIndex = rightPos
			if shrinkS[leftIndex][0] == shrinkS[rightIndex][0] and shrinkS[leftIndex][1] <= shrinkS[rightIndex][1]:
				leftIndex += 1
				rightIndex -= 1
				while leftIndex < rightIndex:
					if shrinkS[leftIndex][0] == shrinkS[rightIndex][0] and shrinkS[leftIndex][1] == shrinkS[rightIndex][1]:
						leftIndex += 1
						rightIndex -= 1
					else:
						break
				if rightIndex <= leftIndex:
					break
		rightIndex = 0
		for i in xrange(0, rightPos):
			rightIndex += shrinkS[i][1]
		rightIndex += shrinkS[0][1]			
		addString = []
		index = length - 1
		while index >= rightIndex:
			addString.append(s[index])
			index -= 1
		#print addString
		#print rightIndex
		return "".join(addString) + s
so = Solution()
s = "aba"
s = "aacecaaa"
print so.shortestPalindrome(s)