class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
	def combinationSum(self, candidates, target):
		candidates = sorted(candidates)
		if candidates == []:	return []
		nums = []
		nums.append(candidates[0])
		for i in xrange(1, len(candidates)):
			if candidates[i] != nums[-1]:
				nums.append(candidates[i])
		result = []
		numPath = []
		self.getCombinationSum(nums, target, result, numPath)
		return result
	def getCombinationSum(self, nums, target, result, numPath):
		if nums == []: return
		if nums[0] > target:	return
		if target % nums[0] == 0:
			result.append(numPath + [nums[0] for i in xrange(0, target/nums[0])])
		nowNum = []
		while target > 0:
			self.getCombinationSum(nums[1:], target, result,numPath +  nowNum)
			nowNum.append(nums[0])
			target -= nums[0]
so = Solution()
candidates = [7,3,2]
target = 18
print so.combinationSum(candidates, target)