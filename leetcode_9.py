class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = list (str(x))
        c = a.copy()
        b = list(reversed(a))
        if c == b:
            return True
        else :
            return False
