class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        total=0
        left=0
        result=float('inf')
        for right in range(len(nums)):
            total+=nums[right]
            while total>=target:
                total-=nums[left]
                left += 1
            if total + nums[left-1] >= target:
                result = min(result, right - (left-1) + 1)
        return result