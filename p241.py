class Solution:
	op = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}
    # @param {string} input
    # @return {integer[]}
	def diffWaysToCompute(self, input):
		op = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}
		nums = []
		ops = []
		index = 0
		length = len(input)
		if length == 0:	return []
		while index < length:
			num = 0
			while index < length and input[index] >= '0' and input[index] <= '9':
				num = 10 * num + int(input[index])
				index += 1
			nums.append(num)
			if index == length: break
			ops.append(input[index])
			index += 1
		length = len(nums)
		#print nums
		if length == 1:	return [nums[0]]
		cache = [[[] for i in xrange(0, length)] for j in xrange(0, length)]
		for i in xrange(0, length):
			cache[i][i] = [nums[i]]
		for gap in xrange(1,length):
			for i in xrange(0, length-gap):
				cache[i][i+gap] = [Solution.op[ops[t]](left,right) for t in xrange(i,i+gap) for left in cache[i][t] for right in cache[t+1][i+gap] ]
		return cache[0][length - 1]
so = Solution()
input = "0+1"
print so.diffWaysToCompute(input)