class Solution:
    # @param {integer} n
    # @return {integer}
	def trailingZeroes(self, n):
		result = 0
		while n > 1:
			n = n/5
			result += n
		return result