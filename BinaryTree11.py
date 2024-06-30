# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left and root.right is None:
            return 1+self.countNodes(root.left)
        if root.right and root.left is None:
            return 1+self.countNodes(root.right)
        if root.left and root.right:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)