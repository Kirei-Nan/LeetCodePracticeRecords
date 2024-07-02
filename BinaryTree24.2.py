# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result=float('inf')
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        if root.left:
            if root.val-root.left.val<self.result:
                self.result=root.val-root.left.val
        if root.right:
            if root.right.val-root.val<self.result:
                self.result=root.right.val-root.val
        self.getMinimumDifference(root.left)
        self.getMinimumDifference(root.right)
        return self.result