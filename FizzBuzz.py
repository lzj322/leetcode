'LeetCode 412 Fizz Buzz'
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rlist=[str(x) for x in list(range(1,n+1))]
        for i in range(1,int(n/3)+1):
            rlist[3*i-1]="Fizz"
        for i in range(1,int(n/5)+1):
            if not i*5%3:
                # rlist[5*i-1].extend("Buzz")
                rlist[5*i-1]="FizzBuzz"
            else:
                rlist[5*i-1]="Buzz"
        return rlist


if __name__ == '__main__':
    s=Solution()
    n=27
    print (s.fizzBuzz(n))
    ss=[1,2,3]
    s2=["1","2","3"]
    a="happy"
    b="new year"
    c=a+b
    print (c)
    sp=str(ss)
    print (s2)
    # print (range(1))







