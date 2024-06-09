class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = []

        for i in range(len(nums) * 2):
            while stack and nums[i % len(nums)] > nums[stack[-1]]:
                result[stack.pop()] = nums[i % len(nums)]
            if i < len(nums):
                stack.append(i)

        return result