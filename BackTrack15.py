class Solution(object):
    def backtrack(self,nums,path,result,used):
        if len(path)==len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]==True:
                continue
            used[i]=True
            path.append(nums[i])
            self.backtrack(nums,path,result,used)
            path.pop()
            used[i]=False
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        used=[False]*(len(nums))
        self.backtrack(nums,[],result,used)
        return result