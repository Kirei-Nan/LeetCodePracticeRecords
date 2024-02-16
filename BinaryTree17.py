# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.path=[]
        self.result=[]
    def traverse(self, node,count):
        if not node.left and not node.right and count==0:
            self.result.append(self.path[:])
            return

        if node.left:
            self.path.append(node.left.val)
            self.traverse(node.left, count - node.left.val)
            self.path.pop()

        if node.right:
            self.path.append(node.right.val)
            self.traverse(node.right, count-node.right.val)
            self.path.pop()

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return self.result
        self.path.append(root.val)
        self.traverse(root, targetSum-root.val)
        return self.result