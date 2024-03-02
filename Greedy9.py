class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        # Apply negation k times
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1

        # If there's an odd number of negations left, apply it to the smallest number
        if k % 2 == 1:
            nums.sort()  # Re-sort the array to find the new smallest number
            nums[0] = -nums[0]

        return sum(nums)

