'LeetCode 263 ugly_number'

class Solution(object):
    def isUgly(self, n):
        """
        :type num: int
        :rtype: bool
        """
        while n>1:
            if n%2 == 0:
               n = n/2
            else:
                break
        while n>1:
            if n%3 == 0:
                n = n/3
            else:
                break
        while n>1:
            if n%5 == 0:
                n = n/5
            else:
                break
        return n==1
	        

if __name__ == '__main__':
    s=Solution()
    n=14
    d=s.isUgly(n)
    print (d)
