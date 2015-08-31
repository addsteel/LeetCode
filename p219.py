class Solution:
	# @param {integer[]} nums
	# @param {integer} k
	# @param {integer} t
	# @return {boolean}
	def containsNearbyAlmostDuplicate(self, nums, k, t):
		length = len(nums)
		if t < k:
			dic = {}
			for i in xrange(0,length):
				if nums[i] in dic and i - dic[nums[i]] <= k:
					return True
				for j in xrange(0,t+1):
					dic[nums[i] + j] = i
					dic[nums[i] - j] = i
		else:
			for i in xrange(0, length):
				for j in xrange(1, k+1):
					if i + j < len(nums) and abs(nums[i+j] - nums[i]) <= t:
						return True
					if i - j >= 0 and abs(nums[i-j] - nums[i]) <= t:
						return True
		return False