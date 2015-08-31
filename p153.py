class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if len(nums) == 0:  return 0
        if len(nums) == 1:  return nums[0]
        if len(nums) == 2:  return min(nums[0], nums[1])
        mid = len(nums)/2
        if nums[mid] > nums[0]:
            return min(nums[0], self.findMin(nums[mid+1:]))
        return self.findMin(nums[0:mid+1])