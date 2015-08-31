class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
	def findKthLargest(self, nums, k):
		k = len(nums) - k
		return self.partition(nums, k)
	def partition(self, nums, k):
		if k < 0 or k >= len(nums):	return -1
		partitionNum = nums[0]
		left = 0
		right = len(nums)
		while left < right:
			right -= 1
			while right > left and nums[right] > partitionNum:
				right -= 1
			if left == right:
				break;
			nums[left] = nums[right]
			left += 1
			while left < right and nums[left] < partitionNum:
				left += 1
			if left < right:
				nums[right] = nums[left]
		nums[left] = partitionNum
		if left == k:	return nums[left]
		elif left > k:
			return self.partition(nums[0:left], k)
		else:
			return self.partition(nums[left+1:],k-left-1)
so = Solution()
nums = [3,1,2]
print so.findKthLargest(nums,1)
print so.findKthLargest(nums,2)
print so.findKthLargest(nums,3)