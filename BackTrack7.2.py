class Solution:
    def backtracking(self,candidates: List[int], target: int, path: List[int], result:List[List[int]],startIndex:int,sum:int )->None:
        if sum>target:
            return
        if sum==target:
            result.append(path[:])
            return
        for i in range(startIndex,len(candidates)):
            sum+=candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates,target,path,result,i,sum)
            sum-=candidates[i]
            path.pop()
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        self.backtracking(candidates,target,[],result,0,0)
        return result