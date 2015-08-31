import math
class Solution:
    # @param {integer} n
    # @return {integer}
	def countPrimes(self, n):
		if n <= 2:	return 0
		primes = [True for i in xrange(0,n)]
		primes[0] = False
		primes[1] = False
		result = 0
		sqrtN = int(math.sqrt(n))
		for i in xrange(2, sqrtN+1):
			if primes[i] == True:
				result += 1
				t = i * i
				while t < n:
					primes[t] = False
					t += i
		for i in xrange(sqrtN+1, n):
			if primes[i] == True:
				result += 1
		return result
n = 16
so = Solution()
print so.countPrimes(n)