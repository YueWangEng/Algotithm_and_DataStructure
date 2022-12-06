## Find median
给出一个有序数列随机旋转之后的数列，如原有序数列为：[0,1,2,4,5,6,7] ，旋转之后为[4,5,6,7,0,1,2]。
假定数列中无重复元素，且数列长度为奇数。
求出旋转数列的中间值。如数列[4,5,6,7,0,1,2]的中间值为4。

### Solution 1:
Sorted, then find the median (not recommend)
```python
list1 = [4,5,6,7,0,1,2]

def median(ll):
    return sorted(ll)[len(ll)//2]

print(median(list1))
```

### Solution 2: -> best
No need to sort, find the median by searching the rotate point.
```python
list1 = [10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def median(ll):
    start, end, n = ll[0], ll[-1], len(ll)
    if start < end:
        return ll[n // 2]
    else:
        for i in range(1, n):
            if start >= ll[i]:
                if i <= n // 2:
                    return ll[(n - 1 + (2 * i - 1)) // 2 + 1]
                else:
                    return ll[(2 * i - n) // 2]
                break

print(median(list1))
```
