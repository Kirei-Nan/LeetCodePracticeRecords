# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left:
            return root.left.val
        if root.right:
            return 0
        if root.left:
            leftsum=self.sumOfLeftLeaves(root.left)
        if root.right:
            rightsum=self.sumOfLeftLeaves(root.right)
        return leftsum+rightsum
