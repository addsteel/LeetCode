class Solution:
	# @param {integer[]} nums
	# @return {integer[][]}
	def fourSum(self, nums, target):
		result = []
		length = len(nums)
		nums.sort()
		#print nums
		i = 0
		while i < length - 1:
			j = i + 1
			while j < length - 1:
				sum = nums[i] + nums[j]
				left = j+1
				right = length - 1
				while left < right:
					if nums[left] + nums[right] + sum > target:
						right -= 1
					elif nums[left] + nums[right] + sum < target:
						left += 1
					else:
						result.append((nums[i], nums[j], nums[left], nums[right]))
						while left < right and nums[left] == nums[left+1]:
							left += 1
						while left < right and nums[right] == nums[right-1]:
							right -= 1
						left += 1
						right -= 1
				while j < length - 1 and nums[j] == nums[j+1]:
					j += 1
				j += 1
			while i < length - 1 and nums[i] == nums[i+1]:
				i += 1
			i += 1
		return result