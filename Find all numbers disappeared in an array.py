'LeetCode 448 Find All Numbers Disappeared in an Array'
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     index = abs(nums[i]-1)
        #     nums[index] = -abs(nums[index])
        # print (nums)
        # return [i+1 for i in range(len(nums)) if nums[i]>0]
        ans=[]
        for item in nums:
            val = abs(item)-1
            if nums[val]>0:
                nums[val]=-nums[val]
            print (val,nums)

        for i in range(len(nums)):
            if nums[i]>0:
                ans.append(i+1)
        return ans

if __name__ == '__main__':
    s=Solution()
    c=[4,3,2,7,8,2,3,1]
    d=[2]
    print (s.findDisappearedNumbers(c))
    # p=list(set(c))
    # print (p)
    # an=[n for n in c if n not in p]
    # print (list(range(1,4)))
    # print (an)







