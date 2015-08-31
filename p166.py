class Solution:
    def div(self, dividend, divider):
            result = ""
            dic = {}
            #dic[dividend/10] = 0
            #print dividend,divider
            #dic[dividend] = 0
            while dividend is not 0:
                length = len(result)
                num = 0
                if dividend in dic:
                    #print result
                    break
                if dividend > divider and dic == {}:
                    dic[dividend] = 0
                while dividend < divider:
                    dic[dividend] = length+num
                    #print dividend
                    dividend *= 10
                    num += 1
                result += "0" * num
                #print result
                result = result + str(dividend / divider)
                #print result
                #print result
                dividend = dividend % divider
                if dividend in dic:
                    
                    break
                #print dividend
                dic[dividend] = len(result)
                #print dividend, dic[dividend]
                dividend = dividend * 10
                #print dividend, result
                
            #print dividend
            if dividend is 0:
                return result
            else:
                return result[0:dic[dividend]] + '(' + result[dic[dividend]:] + ')'
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0:
            return "NA"
        if numerator == 0:
            return "0"
        sign = ""
        if numerator < 0 ^ denominator < 0:
            sign = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        if numerator % denominator is not 0:
            return sign + str(numerator/denominator) + '.' + self.div(10 * (numerator % denominator), denominator)
        else:
            return sign + str(numerator/denominator)
so = Solution()
#print "hello world"
print so.fractionToDecimal(1,90)