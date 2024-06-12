class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result=float('inf')
        sum = 0
        i=0
        for j in range(0,len(nums)):
            sum+=nums[j]
            while sum>=target:
                sum-=nums[i]
                result=min(result,j-i+1)
                i+=1
        return result if result != float('inf') else 0