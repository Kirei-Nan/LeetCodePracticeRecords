# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val==key:
            if root.left is None and root.right is None:
                return root
            elif root.left is None and root.right:
                return root.right
            elif root.right is None and root.left:
                return root.left
            else:
                cur=root.right
                while cur.left:
                    cur=cur.left
                cur.left=root.left
                return cur
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root

