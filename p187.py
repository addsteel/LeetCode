class Solution:
    # @param {string} s
    # @return {string[]}
	def findRepeatedDnaSequences(self, s):
		result = []
		hash = set()
		inResult = set()
		bound = len(s) - 9
		if bound < 2:	return result
		charMapNum = {'A':1,'T':2, 'C':3, 'G': 4}
		powerFour = [2*i for i in xrange(0,10)]
		powerFour = tuple(powerFour)
		hashNum = 0
		for i in xrange(0, 10):
			#print hashNum
			hashNum += charMapNum[s[i]] << powerFour[i]
			print hashNum
		#print hashNum
		hash.add(hashNum)
		for i in xrange(1, bound):
			hashNum = ((hashNum - charMapNum[s[i-1]])>>2) + (charMapNum[s[i+9]] << powerFour[9])
			#print hashNum
			if hashNum in hash and hashNum not in inResult:
				result.append(s[i:i+10])
				inResult.add(hashNum)
			else:
				hash.add(hashNum)
		return result
so = Solution()
print so.findRepeatedDnaSequences("AAAAAAAAAAAAAAAAAAAAAAAAAA")