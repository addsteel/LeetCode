class Solution:
# @param {integer} m
# @param {integer} n
# @return {integer}
	def rangeBitwiseAnd(self, m, n):
		if m == n:
			return m
		print m^n
		print bin(m^n)
		print len(bin(m^n))
		zeros = len(bin(m^n)) - 2
		print zeros
		return (n >> zeros)<<zeros
so = Solution()
print so.rangeBitwiseAnd(11,15)
