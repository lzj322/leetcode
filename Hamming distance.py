'LeetCode 461 Hamming Distance'
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a=x^y
        count=0
        while a:
            count=count+a%2
            a=int(a/2)
        return count


if __name__ == '__main__':
    s=Solution()
    c=3
    d=2
    print (s.hammingDistance(c,d))
    print (bin(c^d).count('1'))






