'LeetCode 226 Invert Binary Tree'
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root



    def inorderTravesal(self, root):
        result=[]
        if root:
            result+=self.inorderTravesal(root.left)
            result.append(root.val)
            # print (root.val,result)
            result+=self.inorderTravesal(root.right)
        else:
            pass
        return result


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
    str1=str(s21.val)
    pp=str1+'->'
    p=TreeNode(1)
    p21=TreeNode(2)
    p22=TreeNode(3)
    p31=TreeNode(5)
    p.left=p21
    p.right=p22
    p21.left=p31
    # print (ans.invertTree(p))
    # t=list(range(1,5))
    # t.append(6)
    # print (t)
    # print (ans.inorderTravesal(p))
    t=ans.invertTree(s31)
    print (ans.inorderTravesal(t))




