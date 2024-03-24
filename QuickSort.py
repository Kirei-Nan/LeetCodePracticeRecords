def quick_sort(nums):
    if len(nums)<1:
        return nums
    pivot=nums[(len(nums)//2)]
    left=[x for x in nums if x<pivot]
    middle=[x for x in nums if x==pivot]
    right=[x for x in nums if x>pivot]
    return quick_sort(left)+middle+quick_sort(right)

nums=[1,3,0,5,7,2,1,4]
print(quick_sort(nums))