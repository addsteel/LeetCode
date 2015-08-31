class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
		if n <= 0: return 0
		n += 1
		tenPower = []
		#ninePower = []
		tenPower.append(1)
		#ninePower.append(1)
		for i in xrange(1,32):
			tenPower.append(tenPower[-1]*10)
			#ninePower.append(ninePower[-1]*9)
			#print tenPower[-1], ninePower[-1]
		decDeg = 1
		deg = 0
		while n / decDeg > 9:
			decDeg *= 10
			deg += 1
		result = 0
		#print decDeg
		while decDeg > 1:
			#print n
			digit = n / decDeg 
			#print deg
			if digit > 1:
				result += digit * deg * tenPower[deg-1] + decDeg
			elif digit == 1:
				result += deg * tenPower[deg-1] + n - decDeg
			print result
			n =  n - decDeg * digit
			decDeg /= 10
			deg -= 1
		if n > 1: result += 1
		return result
so = Solution()
print so.countDigitOne(100)