### Bubble Sort
Sort from right to left

```python
l = [11,4,5,6,9]

def bubbleSort(lista):
    lena = len(lista)
    for i in range(lena-1): #the times needed to be executed
        for j in range(lena-1 -i): #the part to be executed, the part which already has been sorted will put at the end
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j] #this is for acending, if decending, use '<'.
    return lista

# Sometime, the sort has already been finished on some step and there is no need to the next steps.
def bubbleSortOpt(lista):
    lena = len(lista)
    for i in range(lena-1): 
        exchange = False    #set an flag bit for checkging whether soring has been finished.
        for j in range(lena-1 -i): 
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                exchange = True
        if not exchange:
            return lista
    return lista

if __name__ == '__main__':
    print (bubbleSort(l))
```
