# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None

        rootval=postorder[-1]
        root = TreeNode(rootval)

        seperator=inorder.index(rootval)
        left_inorder=inorder[:seperator]
        right_inorder=inorder[seperator+1:]

        left_postorder=postorder[:len(left_inorder)]
        right_postorder=postorder[len(left_inorder):len(postorder)-1]

        root.left=self.buildTree(left_inorder,left_postorder)
        root.right=self.buildTree(right_inorder,right_postorder)
        return root