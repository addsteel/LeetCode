class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        length = len(gas)
        front = 0
        #cur = 0
        sum = 0
        for i in xrange(0,length):
            sum += gas[i] - cost[i]
        if sum < 0:
            return -1
        while front < length:
            gap_num = 0
            index = front
            while gap_num + gas[index]-cost[index]>= 0:
                gap_num += gas[index]-cost[index]
                index += 1
                if index >= length:
                    return front
            front = index + 1
            #gap[cur] = gap_num + gap[index]
            #cur += 1
        return -1
so = Solution()
print so.canCompleteCircuit([1], [1])