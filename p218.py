class Solution:
	# @param {integer[]} nums
	# @return {boolean}
	def containsNearbyDuplicate(self, nums, k):
		dic = {}
		for i in xrange(0,len(nums)):
			if nums[i] in dic and i - dic[nums[i]] <= k:
				return True
			dic[nums[i]] = i
		return False