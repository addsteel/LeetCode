class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
	def combinationSum2(self, candidates, target):
		candidates = sorted(candidates)
		result = []
		numPath = []
		self.getCombinationSum(candidates, target, result, numPath)
		return result
	def getCombinationSum(self, nums, target, result, numPath):
		if nums == []: return
		if nums[0] > target:	return
		if target == nums[0]:
			result.append(numPath + [nums[0]])
			return
		index = 0
		while index < len(nums) and nums[index] == nums[0]:
			index += 1
		if target % nums[0] == 0 and target / nums[0] <= index:
			result.append(numPath + [nums[0] for i in xrange(0, target/nums[0])])
		nowNums = []
		for i in xrange(0, index+1):
			if target - i * nums[0] < 0:	return
			self.getCombinationSum(nums[index:], target - i * nums[0], result,numPath + nowNums)
			nowNums.append(nums[0])
		return