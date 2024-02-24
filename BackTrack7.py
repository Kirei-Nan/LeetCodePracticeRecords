class Solution(object):
    def __init__(self):
        self.result = []
        self.path = []
    def backtrack(self,candidates,target,path,result,startIndex):
        if sum(path) > target:
            return
        if sum(path)==target:
            result.append(path[:])
            return

        for i in range(startIndex,len(candidates)):
            path.append(candidates[i])
            self.backtrack(candidates,target,path,result,i)
            path.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.backtrack(candidates,target,self.path,self.result,0)
        return self.result
