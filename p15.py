class Solution:
	# @param {integer[]} nums
	# @return {integer[][]}
	def threeSum(self, nums):
		result = []
		length = len(nums)
		nums.sort()
		#print nums
		i = 0
		while i < length - 1:
			left = i+1
			right = length - 1
			while left < right:
				if nums[left] + nums[right] + nums[i] > 0:
					right -= 1
				elif nums[left] + nums[right] + nums[i] < 0:
					left += 1
				else:
					result.append((nums[i], nums[left], nums[right]))
					while left < right and nums[left] == nums[left+1]:
						left += 1
					while left < right and nums[right] == nums[right-1]:
						right -= 1
					left += 1
					right -= 1
			while i < length - 1 and nums[i] == nums[i+1]:
				i += 1
			i += 1
		return result
	# @param {integer[]} nums
	# @return {integer[][]}
	def twoSum(self, nums, target):
		nums.sort()
		#print nums
		left = 0
		right = len(nums) - 1
		result = []
		while right > left:
			if nums[left] + nums[right] > target:
				right -= 1
			elif nums[left] + nums[right] < target:
				left += 1
			else:
				result.append([nums[left],nums[right]])
				while left+1 < right and nums[left+1] == nums[left]:
					left += 1
				left += 1
		return result
#nums = [-1,0,1,2,-1,-4]
#nums = [0, 1, 1, 1, 0 , 1, 0, -1, ]
nums = [0, 0, 0, 0,0,0,0,0, 1,1,1,1,1,1,-1,-1,-1,1-1]
#nums = [1,1,1,1,]
#nums = [3,2,-1,-3,-5,0,-5,-4,-4,2,3]
#nums = [0,0,0]
so = Solution()
#print so.twoSum(nums, 1)
print so.threeSum(nums)