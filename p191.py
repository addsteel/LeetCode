class Solution:
    # @param n, an integer
    # @return an integer
	def hammingWeight(self, n):
		bitsMap = [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]
		i = 0
		result = 0
		while n != 0:
			result += bitsMap[n& 15]
			n = n >> 4
		return result
so = Solution()
print so.hammingWeight(31)