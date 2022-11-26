## Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

### Solution 1 (Three pointers):

```python
import random

l1 = sorted(random.choices([i for i in range(100)], k = 3))
l2 = sorted(random.choices([i for i in range(100)], k = 5))

def sortTwoList(l1, l2):
    l1 += l2      #build new list based on l1, i.e., expand l1.
    f1, r1, r2 = len(l1)-1, len(l1)-len(l2)-1, len(l2)-1      #Three pointers, point to the end of new list, l1, l2 respectively.
    while r1 >=0 and r2 >= 0:
        if l1[r1]>= l2[r2]:         #Compare the lasr umcompared value of l1 and l2, put the big one to the end of unsorted part of new list
            l1[f1] = l1[r1]
            f1 -= 1
            r1 -= 1   
        else:
            l1[f1] = l2[r2]
            f1 -= 1
            r2 -= 1

    if r2>= 0:      #in case that there are still last uncompared element (here all uncompared values are smaller that the values in the new list. So just replace them in the begining part of new list
        l1 = l2[:r2+1]+l1[r2+1:]

    return l1

print(new_sortTwoList(l1,l2))
```

### Solution 2 (improved method): -> best

```python
def new_sortTwoList(l1, l2):
    l1 += l2
    f1, r1, r2 = len(l1)-1, len(l1)-len(l2)-1, len(l2)-1
    while r2 >= 0:          #本题以l1为基础，目的是将l2按顺序加入l1中，不必去分析l2中的值用完以后的情况(此时r2 = -1)，这种情况下，已经排列好。
        if r1 >= 0:
            if l1[r1]>= l2[r2]:
                l1[f1] = l1[r1]
                f1 -= 1
                r1 -= 1   
            else:
                l1[f1] = l2[r2]
                f1 -= 1
                r2 -= 1
        else:           #此时，原l1中的值用完了(r1 = -1)，但l2依然有值，这意味着现l1，前面的一部分值需直接用l2剩余的值去替换。
            l1[r2] = l2[r2]
            r2 -= 1

    return l1
```
