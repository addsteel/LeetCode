class Solution:
    # @param {integer} n
    # @return {boolean}
	def isHappy(self, n):
		if n < 1000:
			hash = set()
			while n not in hash:
				hash.add(n)
				n = self.getSquareSum(n)
				if n == 1:	return True
			return False
		n = self.getSquareSum(n)
		return self.isHappy(n)
	def getSquareSum(self, n):
		result = 0
		while n > 0:
			result += (n % 10)**2
			n /= 10
		return result