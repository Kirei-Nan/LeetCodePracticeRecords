# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return None
        if not root.left and not root.right:
            return root.val
        leftvalue=self.findBottomLeftValue(root.left)
        rightvalue=self.findBottomLeftValue(root.right)
        result=None
        if leftvalue:
            result=leftvalue
        else:
            result=rightvalue
        return result
