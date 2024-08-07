class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record={}

        for i in range(len(nums)):
            if target-nums[i] in record:
                return [record[target-nums[i]],i]
            else:
                record[nums[i]]=i