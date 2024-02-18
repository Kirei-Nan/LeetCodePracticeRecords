# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left:
            if root.val > root.left.val:
                return True
            return self.isValidBST(root.left)
        if root.right:
            if root.val < root.right.val:
                return True
            return self.isValidBST(root.right)

        return False