'LeetCode 257 binary tree paths'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result=[]
        if not root:
            return []
        for path in self.binaryTreePaths(root.left):     
            result += [str(root.val)+'->'+path]
        for path in self.binaryTreePaths(root.right):
            result += [str(root.val)+'->'+path]
        return result or [str(root.val)] 
        
        # cpath=''
        # if not root:
        #     return ''
        # else:
        #     return map(lambda x:cpath+str(root.val)+'->'+x,[self.binaryTreePaths(root.left),self.binaryTreePaths(root.right)])
        # if root.left:
        #     cpath = cpath+str(root.val)+'->'
        #     return self.binaryTreePaths(root.left)
        # if root.right:
        #     cpath = cpath+str(root.val)+'->'
        #     return self.binaryTreePaths(root.right)            



        
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
    # print (ans.binaryTreePaths(s))
    str1=str(s21.val)
    pp=str1+'->'
    p=TreeNode(1)
    p21=TreeNode(2)
    p22=TreeNode(3)
    p31=TreeNode(5)
    p.left=p21
    p.right=p22
    p21.left=p31
    # print (list(map(lambda x:pp+x,[p1,p2])))
    # ans.binaryTreePaths(p)
    print (ans.binaryTreePaths(p))
    # dd=['1']
    # dd+=['2']
    # print (dd)
    # print ([1,2,3,4] or 1)
    # print (ans.binaryTreePaths(s))
    # print (['dfd'+path for path in p3])
    # print ([path for path in p3])
    # str2=s21.val.append("->")

