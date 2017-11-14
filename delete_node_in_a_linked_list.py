'LeetCode 237 Delete Node in a Linked List'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next


if __name__ == '__main__':
    s=Solution()
    c1=ListNode(5)
    c2=ListNode(6)
    c3=ListNode(7)
    c4=ListNode(8)
    print (s.deleteNode(7))
    print (list(map(s.canWinNim,sample)))




