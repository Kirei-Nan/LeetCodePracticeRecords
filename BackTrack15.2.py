class Solution:
    def backtracking(self,nums: List[int],path:List[int],result:List[List[int]],used:List[bool]):
        if len(path[:])==len(nums):
            result.append(path[:])
        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i]=True
            self.backtracking(nums,path,result,used)
            path.pop()
            used[i]=False


    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        used=[False]*len(nums)
        self.backtracking(nums,[],result,used)
        return result