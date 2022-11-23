## Description
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

### Solution 1 (Two Pointers):
This is the optimal solution for the question. Two points: left for 0 and right for 2. Current pointer (cur) traverses the list. if 0, then swap it with value left, and if 2, then swap it with value with right.

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, cur, right = 0, 0, len(nums)-1
        while cur <= right:
            if nums[cur] == 0:
                if cur != left:         #It's aslo okay without the judgement, but slightly repetitive.
                    nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
                cur += 1      #cur is always infornt of lef, and the list is sorted from left to right, so the value from left should only be 1.
            elif nums[cur] == 1:
                cur += 1
            else:
                if cur != right:            ##It's aslo okay without the judgement, but slightly repetitive.
                    nums[right], nums[cur] = nums[cur], nums[right]
                right -= 1      #Here cur can not move head, as the value from right is uncertain, 0, 1 or 2. Should check one more time.
                
        return nums
```

###  Solution 2 (1 pointer):
There are 2 traversals needed, one for sorting 0, the other one for sorting 1.

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[cur], nums[i] = nums[i], nums[cur]
                cur += 1
        for i in range(cur, len(nums)):
            if nums[i] == 1:
                nums[cur], nums[i] = nums[i], nums[cur]
                cur += 1
        return nums
```
