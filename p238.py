class Solution:
	# @param {integer[]} nums
	# @return {integer[]}
	def productExceptSelf(self, nums):
		length = len(nums)
		#if length < 2:	return []
		result = [1 for i in xrange(0, length)]
		for i in xrange(1, length):
			result[length-1] = nums[i-1]*result[length-1]
			result[i] = result[length-1]
		for i in xrange(1,length-1):
			result[0] = result[0] * nums[length - i]
			result[length-i-1] = result[length-i-1] * result[0]
		result[0] = result[0] * nums[1]
		return result
so = Solution()
#nums = [1,2,3,4]
nums = [0, 0]
print so.productExceptSelf(nums)