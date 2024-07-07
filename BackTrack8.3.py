class Solution:
    def backtracking(self,candidates: List[int], target: int, path:List[int], result: List[List[int]],startIndex:int,sum:int):
        if sum==target:
            result.append(path[:])
            return
        record = set()
        for i in range(startIndex,len(candidates)):
            if candidates[i] in record:
                continue
            path.append(candidates[i])
            sum+=candidates[i]
            record.add(candidates[i])
            self.backtracking(candidates,target,path,result,i+1,sum)
            path.pop()
            sum-=candidates[i]
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        self.backtracking(candidates,target,[],result,0,0)
        return result