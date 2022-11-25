### Insertion sort
Sort from left to right

```python
import random

lista = random.choices([i for i in range (100)], k=10)          #build a list with random numbers
print(lista)

def insertionSort(ll):
    
    for i in range (1, len(ll)):           # sort from left to right        
        j = i -1            #pointer j is infront of pointer i
        temp = ll[i]            #save value of i, later the value on postion i may be changed.
        while j >= 0:           
            if ll[j] <= temp:           #no need for changes
                break
            else:           #swap value, continue to traverse forward until ll[j] <= temp
                ll[j+1], ll[j] = ll[j], temp
                j -= 1
        print (ll)

    return ll

print(insertionSort(lista))
```
