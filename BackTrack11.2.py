class Solution:
    def backtracking(self,nums,path,result,startIndex):
        result.append(path[:])
        for i in range(startIndex,len(nums)):
            path.append(nums[i])
            self.backtracking(nums,path,result,i+1)
            path.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.backtracking(nums,[],result,0)
        return result