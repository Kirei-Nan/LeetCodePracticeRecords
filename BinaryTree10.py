# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        minleft = float('inf')
        minright = float('inf')

        if root.left:
            minleft=self.minDepth(root.left)
        if root.right:
            minright=self.minDepth(root.right)
        return 1+min(minleft,minright)