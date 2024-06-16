class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        nums.sort()
        for k in range(len(nums)):
            if k>0 and nums[k]==nums[k-1]:
                continue
            for i in range(k+1,len(nums)):
                left=i+1
                right=len(nums)-1

                if i>k+1 and nums[i] == nums[i - 1]:
                    continue
                while left<right:
                    if nums[k] + nums[i] + nums[left] + nums[right] == target:
                        result.append([nums[k], nums[i], nums[left], nums[right]])

                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1

                        left+=1
                        right-=1
                    elif nums[k] + nums[i] + nums[left] + nums[right] < target:
                        left+=1
                    else:
                        right-=1

        return result

