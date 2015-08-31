class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        if num < 10:    return num
        digitSum = 0
        while num != 0:
            digitSum += num % 10
            num /= 10
        return self.addDigits(digitSum)