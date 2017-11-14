'LeetCode 168 Excel Sheet Column Title'
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        '精彩之处就在于n-1 然后再转字符的时候加上'
        title=""
        while n>26:
            char=chr((n-1)%26+65)
            print (n%26)
            n=int((n-1)/26)
            title=char+title
        return chr(n-1+ord('A'))+title
    def numToTitle(self, n):
        res=''
        base=ord('A')
        while n:
            n,r = divmod(n-1,26)
            print (n,r)
            res ='{}{}'.format(chr(base+r),res)
            print (res)
        return res




if __name__ == '__main__':
    s=Solution()
    c=777
    d=27
    li= list(range(1,79))
    se=[x**2 for x in range(4)]
    # print (se) 
    # print (ord('A'))
    print (s.numToTitle(c))
    # print (s.convertToTitle(d))


