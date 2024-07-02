# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mode=[]
        self.map={}
    def traversal(self,root:Optional[TreeNode])->None:
        if not root:
            return
        self.map[root.val]=self.map.get(0,root.val)+1
        self.traversal(root.left)
        self.traversal(root.right)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal(root)
        max_freq=max(self.map.values())
        for key,freq in self.map.items():
            if freq==max_freq:
                self.mode.append(key)
        return self.mode