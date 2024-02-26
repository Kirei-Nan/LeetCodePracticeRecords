class Solution(object):
    def backtrack(self,nums,path,result,startIndex,used):
        result.append(path[:])
        if len(path) == len(nums):
            return
        for i in range(startIndex,len(nums)):
            if i>0 and nums[i]==nums[i-1] and used[i-1]==False:
                continue
            path.append(nums[i])
            used[i]=True
            self.backtrack(nums,path,result,i+1,used)
            used[i]=False
            path.pop()

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        used=[False]*len(nums)
        nums.sort()
        self.backtrack(nums,[],result,0,used)
        return result