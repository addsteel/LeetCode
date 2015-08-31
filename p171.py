class Solution:
    # @param {string} s
    # @return {integer}
	def titleToNumber(self, s):
		result = 0
		base = ord('A') - 1
		for c in s:
			result = result * 26 + ord(c)- base
		return result
so = Solution()
print so.titleToNumber('AA')