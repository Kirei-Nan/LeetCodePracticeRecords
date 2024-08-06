class Solution:
    def backtracking(self, path, result, startIndex, candidates, target, used):
        if sum(path) == target:
            result.append(path[:])
            return
        for i in range(startIndex, len(candidates)):
            if i>0 and candidates[i]==candidates[i-1] and not used[i-1]:
                continue
            if sum(path)+candidates[i]>target:
                break
            path.append(candidates[i])
            used[i]=True
            self.backtracking(path,result,i+1,candidates,target,used)
            path.pop()
            used[i]=False


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        used=[False]*len(candidates)
        result=[]
        candidates.sort()
        self.backtracking([],result,0,candidates,target,used)
        return result