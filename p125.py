class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length == 0: return True
        s = s.lower()
        left = 0
        right = length - 1
        while left < right:
            while left < right and not s[left].isalpha() and not s[left].isdigit():
                left += 1
            while right > left and not s[right].isalpha() and not s[left].isdigit():
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True