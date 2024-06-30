# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum=0
    def traversal(self,root):
        if not root:
            return
        if root.left:
            if not root.left.left and not root.left.right:
                self.sum += root.left.val
        self.traversal(root.left)
        self.traversal(root.right)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.traversal(root)
        return self.sum