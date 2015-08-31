class Solution:
    # @param {integer} n
    # @return {string}
	def convertToTitle(self, n):
		result = []
		while n > 0:
			c = (n - 1) % 26
			result.append(chr(65+c))
			n = (n-c)/26
		return "".join(result[::-1])
so = Solution()
print so.convertToTitle(52)