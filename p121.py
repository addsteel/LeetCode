class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        maxIndex = 1
        while maxIndex < len(prices) and prices[maxIndex] <= prices[maxIndex-1]:
            maxIndex += 1
        if maxIndex == len(prices): return 0
        prices = prices[maxIndex-1:]
        iMax = prices[0]
        maxIndex = 0
        for i, p in enumerate(prices):
            if p > iMax:
                iMax = p
                maxIndex = i
        iMin = iMax
        for p in prices[:maxIndex]:
            if p < iMin:
                iMin = p
        return max(iMax - iMin, self.maxProfit(prices[maxIndex+1:]),0)
so = Solution()
a = []
for i in xrange(0, 10000):
    a.append(9999-i)
print so.maxProfit(a)