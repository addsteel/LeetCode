class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)
        
        while left < right:
        		mid = (left + right)/2
        		if nums[mid] > target:
        				right = mid - 1
        		else:
        			 	if nums[mid] < target:
        					left = mid + 1
        				else:
        						return mid
        #print left
        if left >= len(nums) and target > nums[-1]:	
        	return len(nums)
        if nums[left] == target:
        		return left
        else:
        		if nums[left] < target:
        			return left+1
        		else:
        				return left
so = Solution()
nums = (1,3,5)
target = 4
print so.searchInsert(nums, target)