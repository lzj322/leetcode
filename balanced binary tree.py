'LeetCode 404 Sum of Left Leaves'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    UNbalanced=-1
    def depth(self, root):
        dep=0
        if not root:
            return 0
        else:
            dep+=1
            return dep+max(self.depth(root.left),self.depth(root.right))   
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return abs(self.depth(root.right)-self.depth(root.left))<1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    def getHeight(self, root):
        if not root:
            return 0
        l=self.getHeight(root.left)
        r=self.getHeight(root.right)
        if l==-1 or r==-1 or abs(l-r)>1:
            return -1
        return 1+max(l,r)
    def isBalanced2(self,root):
        if not root:
            return True
        return self.getHeight(root)!=-1



        
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
    print (ans.depth(s))
    print (ans.isBalanced(s))
