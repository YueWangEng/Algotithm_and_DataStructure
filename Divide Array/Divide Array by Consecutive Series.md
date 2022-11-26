## Divide Array by Consecutive Series
Give a sorted array, find the continuous number range and divide it into different parts.

### Solution:
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
