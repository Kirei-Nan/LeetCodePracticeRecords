# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self,root):
        if not root:
            return 0
        left_height=self.getHeight(root.left)
        if left_height==-1:
            return -1
        right_height=self.getHeight(root.right)
        if right_height==-1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        else:
            return 1 + max(left_height, right_height)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.getHeight(root)!=-1:
            return True
        else:
            return False