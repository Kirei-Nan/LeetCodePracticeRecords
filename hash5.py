class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        records={}
        for i in range(len(nums)):
            if target-nums[i] in records:
                return [i, records[target-nums[i]]]
            else:
                records[nums[i]]=i
        return []