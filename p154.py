class Solution:
    def __init__(self):
        nums = None
        target = 0
        length = 0
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        self.nums = nums
        self.target = target
        self.length = len(nums)
        return self.iSearch(0, self.length)
    def iSearch(self, left, right):
        nums = self.nums
        target = self.target
        if right - left < 3:
            if right - left <= 0:   return -1
            if right - left == 1:
                if nums[left] == target:    return left
                return -1
            if nums[left] == target:
                return left
            elif nums[left+1] == target:
                return left+1
            return -1
        mid = (right+left)/2
        if nums[mid] < nums[left]:
            if target < nums[mid]:
                return self.iSearch(left+1, mid)
            elif target > nums[mid]:
                if target > nums[left]:
                    return self.iSearch(left+1, mid)
                elif target < nums[left]:
                    return self.iSearch(mid+1, right)
                else:
                    return left
            else:
                return mid
        elif nums[mid] > nums[left]:
            if nums[mid] > target:
                if target > nums[left]:
                    return self.iSearch(left, mid)
                elif target < nums[left]:
                    return self.iSearch(mid+1, right)
                else:
                    return left
            elif nums[mid] < target:
                return self.iSearch(mid+1, right)
            else:
                return mid
        else:
            return -1
        return -1