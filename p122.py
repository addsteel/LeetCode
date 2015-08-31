class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        left = 1
        while left < len(prices) and prices[left] <= prices[left-1]:
            left += 1
        right = len(prices) - 1
        while right > 0 and prices[right] <= prices[right-1]:
            right -= 1
        prices = prices[left-1:right+1]
        if len(prices) < 2: return 0
        length = len(prices)
        profile = [0 for i in xrange(0, length)]
        for i in xrange(0, length-1):
            index = length - i - 2
            if prices[index] < prices[-1]:
                profile[index] = prices[-1] - prices[index]
            if profile[index] < profile[index+1]:
                profile[index] = profile[index+1]
            for j in xrange(index+1, length-1):
                if prices[j] > prices[index]:
                    if prices[j] - prices[index] + profile[j+1] > profile[index]:
                        profile[index] = prices[j] - prices[index] + profile[j+1]
                
        return profile[0]