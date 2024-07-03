# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right, key)
        else:
            if root.right and root.left:
                cur = root.right
                while cur.left is not None:
                    cur = cur.left
                cur.left = root.left
                return root.right
            elif root.right and not root.left:
                return root.right
            elif not root.right and root.left:
                return root.left
            else:
                return None
        return root