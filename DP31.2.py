# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val

        val1=root.val
        if root.left:
            val1+=self.rob(root.left.left)+self.rob(root.left.right)
        if root.right:
            val1+=self.rob(root.right.left)+self.rob(root.right.right)
        val2=self.rob(root.left)+self.rob(root.right)
        return max(val1,val2)