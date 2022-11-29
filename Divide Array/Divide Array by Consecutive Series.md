## Divide Array by Consecutive Series
Give a sorted array, find the continuous number range and divide it into different parts.

### Solution 1:
Compare the adjacent elements，if the difference is 1, the they are continuous numbers.

```python
ll = [1, 3, 3, 5, 6, 7, 8, 11, 12, 13, 18,19]
lll = []
l, r = 0, 1

while r < len(ll):
    if ll[r] - ll[r-1] == 1:
        r += 1
    else:
        lll.append(ll[l:r])
        l = r
        r += 1
lll.append(ll[l:])

print(lll)
```

### Solution 2: -> best
Using the function, groupby, in the tool of itertools. In the sorted array, compare the value with the index, continuous number will have the same different.  
Here need to understand the return value of groupby and enumerate.
1) `groupby(squence, func)`: a value and an itertool object. To change the itertool object to list, use `list()`.
2) `enumerate(squence)`: enumerate object, use `list()` to get list, and the element inside of it is tuple.
3) 
```python
ll = [1, 3, 3, 5, 6, 7, 8, 11, 12, 13, 18,19]
from itertools import groupby
lll = []
diff = lambda x: x[1] - x[0]
for dif, l in groupby(enumerate(ll),diff):          
    l1 = [x[1] for x in list(l)]
    lll.append(l1)

print(lll)
```
