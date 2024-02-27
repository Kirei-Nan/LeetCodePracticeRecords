class Solution(object):
    def backtrack(self, nums, path, result,startIndex):
        if len(path)>1:
            result.append(path[:])
        uset=set()
        for i in range(startIndex,len(nums)):
            if ( path and nums[i]<path[-1]) or nums[i] in uset:
                continue

            uset.add(nums[i])
            path.append(nums[i])
            self.backtrack(nums, path, result,i+1)
            path.pop()

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        self.backtrack(nums, [],result,0)
        return result