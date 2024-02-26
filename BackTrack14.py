class Solution(object):
    def isValid(self,path):
        if len(path)<2:
            return False
        prev=None
        for i in path:
            if prev is None:
                prev=i
            else:
                if i<prev:
                    return False
        return True
    def backtrack(self,nums,path,result,startIndex,used):
        if self.isValid(path):
            result.append(path[:])

        for i in range(startIndex,len(nums)):
            if i>0 and used[i-1]==False and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            used[i]=True
            self.backtrack(nums,path,result,i+1,used)
            path.pop()
            used[i]=False


    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used=[False]*len(nums)
        result=[]
        self.backtrack(nums,[],result,0,used)
        return result
