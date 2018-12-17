class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            print (0)
        elif needle in haystack :
            print (haystack.index(needle))
        else:print (-1)
string = Solution()
string.strStr('grwerghhjyujuier','jyu')
## This situation makes result No.8 . 