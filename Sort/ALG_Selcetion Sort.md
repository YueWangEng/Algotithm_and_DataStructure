### Selection sort
Sort from left to right

```python
import random

lista = random.choices([i for i in range (100)], k=10)          #build a list with random numbers
print(lista)
def slectionSort(ll):
    for i in range (len(ll)):           # sort from left right
        minV = min(ll[i:])          #find the minmum number in the unsorted part of the list and put it in the sorted part
        k = ll.index(minV)
        print (k)
        ll[i], ll[k] = ll[k], ll[i]         #before i, it is the sorted part
        print (ll)
    return ll

print(slectionSort(lista))
```
