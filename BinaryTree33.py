# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.pre=None
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        self.convertBST(root.right)
        if self.pre is not None:
            root.val=self.pre.val+root.val
        self.pre=root
        self.convertBST(root.left)
        return root