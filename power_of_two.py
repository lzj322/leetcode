'LeetCode 231 power_of_two'

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return False
        while n>1:
            if n%2:
                return False
            else:
                n=n/2
        return True
    def isPower(self, n):
    	return n>0 and not (n & n-1)

if __name__ == '__main__':
    s=Solution()
    n=-11
    d=s.isPower(n)
    print (d)
