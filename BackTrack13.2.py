class Solution:
    def backtracking(self,nums: List[int],path:List[int],result:List[List[int]],startIndex:int,used:List[bool])->None:
        result.append(path[:])
        for i in range(startIndex,len(nums)):
            if i>0 and nums[i-1]==nums[i] and not used[i-1]:
                continue
            path.append(nums[i])
            used[i]=True
            self.backtracking(nums,path,result,i+1,used)
            path.pop()
            used[i]=False
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used=len(nums)*[False]
        result=[]
        self.backtracking(nums,[],result,0,used)
        return result