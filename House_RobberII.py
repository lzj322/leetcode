'LeetCode 213 House Robber II'
class Solution(object):
    def rob(self, nums):
        def _rob(nums):
            a, b = 0, 0
            for i in range(len(nums)):
                a, b = b, max(a + nums[i], b)
                print (nums[i],a,b)
            return b
        a, b = _rob(nums[:-1]), _rob(nums[1:])
        return max(a, b) if len(nums) is not 1 else nums[0]
        # return depo

if __name__ == '__main__':
    s=Solution()
    c=[7,3,2,5,4,6,4,0,7]
    d=[4,2,4,6,1,1,1,4,6]
    print (s.rob(d))
    print (list(range(len(d))))
    print (c[:-1])





