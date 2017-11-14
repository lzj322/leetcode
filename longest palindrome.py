'LeetCode 409 Longest_Palindrome'

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dhist=dict()
        for c in s:
            dhist[c] = dhist.get(c,0)+1
        nums=dhist.values()
        # print (nums)
        # print ('num of values:',len(nums))
        nsum=0
        # maxodd=0
        flag=0
        for n in nums:
            if n%2:
                nsum+=n-1
                flag=1
            else:
                nsum+=n
        return nsum+flag


if __name__ == '__main__':
    s=Solution()
    t="a"
    r="bananas"
    od="abbbcccddddd"
    hard="civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    # print (set(hard),len(set(hard)))
    print (s.longestPalindrome(od))
    # print (len(hard))


