## Divide Array in Sets of K Consecutive Numbers
Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.
Return true if it is possible. Otherwise, return false.

### Solution 1:

```python
def func(nums, k):
    if len(nums) % k != 0:
        return False
    else:
        from collections import Counter
        dnums = dict(Counter(nums))
        lnums = list(sorted(dnums.keys()))
        print(dnums)
        print(lnums)
        i = 0
        while i < len(lnums):
            print(lnums[i], dnums)
            if dnums[lnums[i]] > 0:
                j = lnums[i]
                while j < lnums[i]+k:
                    if j in dnums and dnums[j] > 0:
                        dnums[j] -= 1
                        j += 1
                    else:
                        return False
            else:
                i += 1
        print (dnums)
        return True
```
