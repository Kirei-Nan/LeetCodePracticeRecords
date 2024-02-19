# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        cur=root
        parent=root
        while cur:
            parent = cur
            if cur.val<val:
                cur=cur.right
            elif cur.val>val:
                cur=cur.left
        node=TreeNode(val)
        if val<parent.val:
            parent.left=node
        else:
            parent.right=node
        return root
