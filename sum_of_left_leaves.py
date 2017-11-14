'LeetCode 404 Sum of Left Leaves'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        s=0
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        
if __name__ == '__main__':
    s=TreeNode(5)
    s21=TreeNode(4)
    s22=TreeNode(8)
    s.left=s21
    s.right=s22
    s31=TreeNode(11)
    s32=TreeNode(13)
    s33=TreeNode(4)
    s21.left=s31
    s22.left=s32
    s22.right=s33
    s41=TreeNode(7)
    s42=TreeNode(2)
    s43=TreeNode(1)
    s31.left=s41
    s31.right=s42
    s33.right=s43
    ans=Solution()
    print (ans.sumOfLeftLeaves(s))
