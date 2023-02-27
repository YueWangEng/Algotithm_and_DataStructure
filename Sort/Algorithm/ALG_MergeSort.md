### Merge Sort

1. 排序方法为将两个排好序的序列合并为一个排序序列
2. 将原长序列不断划分，直到单元素序列，再重新不断合并，所以需要用到递归

```python
import random

li = random.choices([i for i in range(100)], k=16)
print (li)

def merge(li, low, mid, high):  #假定mid两侧部分都是已经按升序排好
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:   #依次选择小的放入到新创建的ltmp
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    
    li[low:high+1] = ltmp

def merge_sort(li, low, high):
    if low < high:  #保证至少要有两个元素
        #print (low, high)
        mid = (low+high) // 2
        merge_sort(li, low, mid) #分段，左侧
        merge_sort(li, mid+1, high) #分段，右侧
        merge(li,low,mid, high) #合并

merge_sort(li, 0, len(li)-1)
print(li)
```
