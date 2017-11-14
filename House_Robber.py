'LeetCode 198 House Robber'
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        depo=[0]*(len(nums)+1)
        # depo=[0,nums[0]]
        depo[1]=nums[0]
        # for i,item in enumerate(nums):
        for i in range(1,len(nums)):
            depo[i+1]=max(depo[i-1]+nums[i],depo[i])
            print (depo[i+1])
        return depo[-1]

if __name__ == '__main__':
    s=Solution()
    c=[7,3,2,5,4,6,4,0,7]
    d=[4,2,4,6,1,1,1,4,6]
    b=[1,7,1,1,6,1,1,9,1]
    print (s.rob(d))





