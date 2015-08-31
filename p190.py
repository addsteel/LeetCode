class Solution:
    # @param n, an integer
    # @return an integer
	def reverseBits(self, n):
		bitsMap = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
		i = 28
		result = 0
		while n != 0:
			result = result | ((bitsMap[n & 15]) << i)
			n = n >> 4
			i -= 4
		return result
so = Solution()
print bin(so.reverseBits(31))