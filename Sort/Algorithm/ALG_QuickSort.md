# Quick Sort

1. 取一个元素p，使元素p归位；
2. 列表被p分为两部分，左边都比p小，左边都比p大；
3. 递归完成排序。

```python
import random

ll = random.choices([i for i in range (100)], k=10)
print(ll)
def partition(li, left, right):
    tmp = li[left]          #将p选为最左侧的元素，保存为tmp，待归位
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp          #left==right时，p完成归位，位置为left
    return left

def quick_sort (li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)         #左侧部分继续归位
        quick_sort(li, mid+1, right)            #右侧部分继续归位

quick_sort(ll, 0 , len(ll)-1)
print (ll)
```
