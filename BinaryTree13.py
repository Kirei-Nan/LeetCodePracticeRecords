class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def traverse(self,root,path,result):
        path.append(root.val)
        if not root.left and not root.right:
            sPath = '->'.join(map(str, path))
            result.append(sPath)
            return
        if  root.left:
            self.traverse(root.left,path,result)
            path.pop()
        if  root.right:
            self.traverse(root.right,path,result)
            path.pop()

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result=[]
        path=[]
        if not root:
            return result
        self.traverse(root,path,result)
        return result

