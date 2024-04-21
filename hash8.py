class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution=set()
        result=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            hash = set()

            for j in range(i + 1, len(nums)):
                complement=target-nums[j]
                if complement in hash:
                    triplet=[nums[i],complement,nums[j]]
                    triplet_tuple=tuple(triplet)

                    if triplet_tuple not in solution:
                        result.append(triplet)
                        solution.add(triplet_tuple)
                hash.add(nums[j])
        return result