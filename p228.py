class Solution:
    # @param {integer[]} nums
    # @return {string[]}
	def summaryRanges(self, nums):
		result = []
		if len(nums) == 0:
			return result
		lastIndex = 0
		for i in xrange(1,len(nums)):
			if nums[i] - nums[i-1] > 1:
				if lastIndex == i - 1:
					result.append(str(nums[lastIndex]))
					lastIndex = i
				else:
					result.append(str(nums[lastIndex])+ '->' + str(nums[i-1]))
					lastIndex = i
		if lastIndex == len(nums)-1:
			result.append(str(nums[lastIndex]))
		else:
			result.append(str(nums[lastIndex]) + '->' + str(nums[len(nums)-1]))
		return result
so = Solution()
#nums = []
nums = [1,2,3,6,7,8,9,11]
#nums = [1]
print so.summaryRanges(nums)