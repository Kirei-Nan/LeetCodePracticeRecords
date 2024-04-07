# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self,node):
        if not node:
            return (0,0)

        left=self.traversal(node.left)
        right=self.traversal(node.right)

        # 不偷当前节点
        val_0=max(left[0],left[1])+max(right[0], right[1])
        # 偷当前节点
        val_1=left[0]+node.val+right[0]
        return (val_0,val_1)
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.traversal(root))

