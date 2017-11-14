'LeetCode 441 arranging coins'
import math
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(((8*n+1)**0.5-1)/2)
        
if __name__ == '__main__':
    s=Solution()
    l=[0,1,2,3,4,5,6,7,8,9]
    ans=list(map(s.arrangeCoins,l))
    print (ans)
