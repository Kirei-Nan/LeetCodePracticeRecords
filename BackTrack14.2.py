class Solution:
    def backtracking(self,nums:List[int],path:List[int],result:List[List[int]],startIndex:int)->None:
        if len(path[:])>=2:
            result.append(path[:])
        record=set()
        for i in range(startIndex,len(nums)):
            if (path and nums[i]<path[-1]) or nums[i] in record:
                continue
            path.append(nums[i])
            record.add(nums[i])
            self.backtracking(nums,path,result,i+1)
            path.pop()
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.backtracking(nums,[],result,0)
        return result