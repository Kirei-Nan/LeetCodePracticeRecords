class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record={}

        for index,value in enumerate(nums):
            complement=target-value
            if complement in record:
                return [index,record[complement]]
            else:
                record[value]=index
        return []