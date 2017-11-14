'LeetCode 292 Nim Game'
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n<4:
        #     return True
        # else:
        #     for i in range(1,4):
        #         print (i)
        #         if not self.canWinNim(n-i):
        #             return True
        #             break
        #     return False
        return (n%4!=0)

if __name__ == '__main__':
    s=Solution()
    c=1
    d=27
    sample = list(range(1,17))
    print (sample)
    print (list(map(s.canWinNim,sample)))




