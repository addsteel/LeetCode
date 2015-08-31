# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 0:    return 0
        result = 0
        for p in points:
            dic = {}
            samePoints = 0
            for q in points:
                if p.x == q.x:
                    if p.y == q.y:
                        samePoints += 1
                    else:
                        if 'Nan' in dic:
                            dic['Nan'] += 1
                        else:
                            dic['Nan'] = 1
                else:
                    key = round((float(p.y - q.y))/(p.x - q.x), 10)
                    #print q.x, q.y, key
                    if key in dic:
                        dic[key] += 1
                    else:
                        dic[key] = 1
                    #print dic[key]
            maxValue = 0
            #print p.x, p.y
            for value in dic.values():
                #print value
                if value > maxValue:
                    maxValue = value
            #break
            maxValue += samePoints
            if maxValue > result:
                result = maxValue
        return result
so = Solution()
p1 = Point(84,250)
p2 = Point(0,0)
p3 = Point(1,0)
p4 = Point(0,-70)
p5 = Point(0,-70)
p6 = Point(1,-1)
p7 = Point(21,10)
p8 = Point(42,90)
p9 = Point(-42,-230)
print so.maxPoints([p1,p2,p3,p4,p5,p6,p7,p8,p9])