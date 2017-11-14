'LeetCode 171 Excel Sheet Column Number'
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num=0
        for l in s:
            num=26*num+(ord(l)-64)
        return num



if __name__ == '__main__':
    s=Solution()
    t='AB'
    print (s.titleToNumber(t))


