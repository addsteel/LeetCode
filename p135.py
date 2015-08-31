class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [1 for rate in ratings]
    def setCandieis(self, bound, candies, ratings):
        i = 1
        candies[0] = 1
        minCandies = 1
        nextBound = 0
        while i < len(ratings):
            if ratings[i-1] == ratings[i]:
                if i == len(ratings) - 1:   return
                for candy in candies[:i]:
                    candy -= minCandies + 1
                if candies[0] < bound:
                    candies[0] = bound
                self.setCandieis(1, candies[i:], ratings[i:])
                return 
            if ratings[i-1] < ratings[i]:
                candies[i] = candies[i-1] + 1
                if i+1 < len(ratings) and ratings[i] > ratings[i+1]:
                    break
            else:
                candies[i] = candies[i-1] - 1
            i += 1
        for candy in candies[:i]:
            candy -= minCandies + 1
        if candies[0] < bound:
            candies[0] = bound
        if i == len(ratings):   return
        self.setCandieis(candies[i], candies[i:], ratings[i:])