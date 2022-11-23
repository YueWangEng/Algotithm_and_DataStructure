## Remove Duplicates from Sorted Array

### Description
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Return k after placing the final result in the first k slots of nums.
**Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.**

### Solution (Two points)
Repeated elements are not necessarily preserved, they will be replaced by subsequent non-repeated elements.

```python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0     # point cur, in front of it, there is no duplicate value.
        for i in range (1, len(nums)):      #point i, using for traverse.
            if nums[i] != nums[i-1]:
                cur += 1
                if i-cur > 0:     #It's okay if there is no judgement, but slightly repetitive.
                    nums[cur] = nums[i]
            
        return(cur+1)
```
