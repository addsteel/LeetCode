class Solution:
    # @param {integer[]} nums
    # @return {integer}
	def rob(self, nums):
		length = len(nums)
		if length == 0:	return 0
		if length == 1:	return nums[0]
		result = []
		result.append(nums[0])
		result.append(max(nums[0], nums[1]))
		for i in xrange(2, length):
			result.append(max(nums[i] + result[i-2], result[i-1]))
		return result[-1]
nums = [1,2,3,4,1]
so = Solution()
print so.rob(nums)
