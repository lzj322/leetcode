'LeetCode 349 Intersection_of_Two_aArrays'

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=set(nums1)
        nums2=set(nums2)
        return list(nums1&nums2)

if __name__ == '__main__':
    s=Solution()
    t=[3,8,4,2,5]
    t2=[4,3,5,7,2,3]
    print (s.intersection(t,t2))


