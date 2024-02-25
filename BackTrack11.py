class Solution(object):
    def backtrack(self,nums,startIndex,path,result):
        result.append(path[:])
        if startIndex>len(nums):
            return
        for i in range(startIndex,len(nums)):
            path.append(nums[i])
            self.backtrack(nums,i+1,path,result)
            path.pop()
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        self.backtrack(nums,0,[],result)
        return result


