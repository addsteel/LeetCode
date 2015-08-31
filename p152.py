class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:  return 0
        if len(nums) == 1:  return nums[0]
        negFirst = -1
        negLast = -1
        negCount = 0
        product = 1
        for i,num in enumerate(nums):
            if num == 0:
                if negCount % 2 == 0:
                    return max(product, self.maxProduct(nums[i+1:]),0)
                else:
                    return max(self.maxProduct(nums[0:i]), self.maxProduct(nums[i+1:]),0)
            if num < 0:
                negLast = i
                negCount += 1
                if negFirst == -1:
                    negFirst = i
            product *= num
        if negCount % 2 == 0:
            return product
        else:
            if negFirst + 1 < len(nums):
                return max(reduce(lambda x,y:x*y, nums[1:negLast],nums[0]),reduce(lambda x,y:x*y, nums[negFirst+2:],nums[negFirst+1]))
            else:
                return reduce(lambda x,y:x*y, nums[1:negLast],nums[0])