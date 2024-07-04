class Solution:
    def backtracking(self,candidates: List[int], target: int, path: List[int], result: List[List[int]],startIndex: int, sum: int,used:List[int])->None:
        if sum>target:
            return
        if sum==target:
            result.append(path[:])

        for i in range(startIndex,len(candidates)):
            if i>startIndex and candidates[i] == candidates[i - 1] and not used[i-1]:
                continue
            path.append(candidates[i])
            sum+=candidates[i]
            used[i]=True
            self.backtracking(candidates,target,path,result,i+1,sum,used)
            used[i] = False
            sum-=candidates[i]
            path.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        used=[False]*len(candidates)
        candidates.sort()
        self.backtracking(candidates,target,[],result,0,0,used)
        return result