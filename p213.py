class Solution:
    # @param {integer[]} nums
    # @return {integer}
	def rob(self, nums):
		if len(nums) < 3:
			if len(nums) == 0:	return 0
			if len(nums) == 1:	return nums[0]
			if len(nums) == 2:	return max(nums[0], nums[1])
		return max(nums[0] + self.rob1(nums[2:-1]), self.rob1(nums[1:]))
	def rob1(self, nums):
		length = len(nums)
		if length == 0:	return 0
		if length == 1:	return nums[0]
		result = []
		result.append(nums[0])
		result.append(max(nums[0], nums[1]))
		for i in xrange(2, length):
			result.append(max(nums[i] + result[i-2], result[i-1]))
		return result[-1]