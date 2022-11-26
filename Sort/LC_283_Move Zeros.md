## Move Zeroes
Given an integer array nums, move all 0's to the end of it **while maintaining the relative order of the non-zero elements**.
Note that you must do this in-place without making a copy of the array.

### Solution 1: (Overwrite methond) -> Best

```python
nums = [0,1,0,3,12]
def new_new_movingZero(ll):
    l, r = 0, 0
    while r < len(ll):
        if ll[r] != 0:          #if pointer r is not 0, then uset the value to overwrite the value of pointer l, and let it skip to next one
            ll[l] = ll[r]
            l += 1
        r += 1
    for i in range(l, len(ll)):         #set the value from l to the end as 0
        ll[i] = 0
        
    return ll

print (new_new_movingZero(nums))
```

### Solution 2: (Swap method)
```python
nums = [0,1,0,3,12]
def new_movingZero(ll):
    l, r = 0, 0
    while r < len(ll):
        if ll[l] != 0:          #if pointer l is not 0, skip to next one
            l += 1
        elif ll[r] != 0:
            ll[l], ll[r] = ll[r], ll[l]     #if pointer l is 0 and pointer r is not 0, then swap
            l += 1            
        r += 1
        
    return ll
```

**PS**: There is one reuquirement, maintaining the relative order of the non-zero elements. If there is not the requirement. The solution can be as below.
```python
nums = [0,1,0,3,12]

def movingZero(ll):
    l, r = 0, len(ll)-1
    while l <= r:
        if ll[l] == 0:
            ll[l], ll[r] = ll[r], ll[l]
            r -= 1
        else:
            l += 1
    
    return ll
```
