'LeetCode 169 Majority Element'
import math
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj=nums[0]
        count=1
        for item in nums:
            if count==0:
                maj=item
                count+=1
            elif maj==item:
                count+=169
            else:
                count-=1
        return maj


        
        # return nums[math.floor(len(nums)/2)]
        return nums[int(len(nums)/2)]

if __name__ == '__main__':
    s=Solution()
    l=[4,3,4,4,3,4,3,4,2,4,4,4,3,2,4,4,4]
    p=[1]
    print (l)
    print (sorted(l))
    print (s.majorityElement(l))
