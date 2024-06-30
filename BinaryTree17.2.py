# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def backtracking(self,root,targetSum,cursum):
        if not root:
            return False
        cursum += root.val
        if not root.left and not root.right:
            if cursum==targetSum:
                return True
            return False

        return self.backtracking(root.left,targetSum,cursum) or self.backtracking(root.right,targetSum,cursum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.backtracking(root,targetSum,0)