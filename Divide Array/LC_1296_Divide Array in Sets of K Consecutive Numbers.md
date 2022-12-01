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
        dnums = dict(Counter(nums))         #get the value-number dictionary from the list. Here no need to change to dict object, Counter object is fine, which inherit from dict class.
        lnums = list(sorted(dnums.keys()))          #sorted key list. Here no need to use functions like dnums.keys() and list(), just sorted the dnums, and the return value is an list
        i = 0
        while i < len(lnums):
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
        return True
```
