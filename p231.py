class Solution:
    # @param {integer} n
    # @return {boolean}
	def isPowerOfTwo(self, n):
		#if n == 0: return True
		base = 1
		while base > 0 and base < n:
			#print base
			base = base << 1
		if base != n:
			return False
		return True
so = Solution()
if so.isPowerOfTwo(0): print 'Yes'