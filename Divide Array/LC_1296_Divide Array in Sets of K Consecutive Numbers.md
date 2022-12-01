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
        while i < len(lnums):           #遍历所有值
            if dnums[lnums[i]] > 0:     #有可取的值（0代表已经没有，负值是不允许的）
                j = lnums[i]
                while j < lnums[i]+k:       #向后遍历再找k个
                    if j in dnums and dnums[j] > 0:         #这些值需要都在，且数量为正（两种情况：要么原来就没有，要么是已经用完了）。
                        dnums[j] -= 1        
                        j += 1
                    else:
                        return False            #原来就没有，或者已经用完了的情况下，返回Flase
            else:
                i += 1
        return True
```
