class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        start=0
        result=float('inf')
        for i in range(len(nums)):
            sum+=nums[i]
            while sum>=target:
                result = min(result, i - start + 1)
                sum-=nums[start]
                start+=1
        return result if result != float('inf') else 0