from collections import deque
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        mergeList = [1]
        list2 = deque([])
        list3 = deque([])
        list5 = deque([])
        sign = 0
        while len(mergeList) < n:
            list2.append(2*mergeList[-1])
            list3.append(3*mergeList[-1])
            list5.append(5*mergeList[-1])
            if list2[0] == mergeList[-1]:
                list2.popleft()
            if list3[0] == mergeList[-1]:
                list3.popleft()
            if list5[0] == mergeList[-1]:
                list5.popleft()
            if list2[0] < list3[0]:
                if list2[0] < list5[0]:
                    mergeList.append(list2[0])
                    list2.popleft()
                else:
                    mergeList.append(list5[0])
                    list5.popleft()
            else:
                if list3[0] < list5[0]:
                    mergeList.append(list3[0])
                    list3.popleft()
                else:
                    mergeList.append(list5[0])
                    list5.popleft()
        return mergeList[-1]
so = Solution()
print so.nthUglyNumber(1000)