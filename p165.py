class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        version1Nums = version1.split('.')
        version2Nums = version2.split('.')
        if len(version1Nums) < 1 and len(version2Nums) < 1:
            return 0
        while len(version1Nums) < len(version2Nums):
            version1Nums.append("0")
        while len(version2Nums) < len(version1Nums):
            version2Nums.append("0")
        length = len(version1Nums)
        if len(version2Nums) < length:
            length = len(version2Nums)
        for i in xrange(0, length):
            if int(version1Nums[i]) > int(version2Nums[i]):
                return 1
            elif int(version1Nums[i]) < int(version2Nums[i]):
                return -1
        return 0
so = Solution()
print so.compareVersion("1", "1.1")
nums = [1,2,3,4,6]
max = -1
secondMax = -1
for i in range(0, len(nums)):
    if nums[i] > secondMax:
        if nums[i] > max:
            max = nums[i]
            secondMax = max
        elif nums[i] != max:
            secondMax = nums[i]