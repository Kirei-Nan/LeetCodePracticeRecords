# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self,depth,node):
        if not node.left and not node.right:
            if depth>self.maxdepth:
                self.maxdepth=depth
                self.result=node.val
            return
        if node.left:
            self.traversal(depth+1,node.left)
        if node.right:
            self.traversal(depth + 1, node.right)

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.maxdepth=float('-inf')
        self.result=None
        self.traversal(0,root)
        return self.result
