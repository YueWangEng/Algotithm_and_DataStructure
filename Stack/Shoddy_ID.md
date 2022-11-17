### Problem Description: Searching Shoddy ID
There is a sequence of IDs，in which the repetive rated of one shoddy ID is higher the 50%. Please find the shoddy ID.

**Mehtod 1**

As the rate of shoddy ID is highter than 50%. Add the element to the stack if the values are same, and delete the element from the stack if the value are different.

```python
ll = [1,2,3,4,5,1,6,1,2,1,3,1,2,3,2,1,1,1,1,1,5,1,1,5,1,5,1,6,17,1,8,1,1,1,1,1,1,1,9]

stack = []
for i in ll:
    if len(stack) == 0:
        stack.append(i)
    else:
        if i == stack[-1]: #这里分两种情况，一种是与水王ID不一样，消除一个水王ID，另一种是两个非水王，这样是两个非水王之间的内耗。
            stack.append(i)
        else:
            stack.pop()
print (stack)
```

**Improved Method**

Usinf stack will improve the space complexity. The is no need to use the stack, instead, using two variables, one is for the value (the stack top value in the method 1) and the other is for the account.

```python
ll = [1,2,3,4,5,1,6,1,2,1,3,1,2,3,2,1,1,1,1,1,5,1,1,5,1,5,1,6,17,1,8,1,1,1,1,1,1,1,9]

theID = None
count = 0
for val in ll:
    if count == 0:
        theID = val
        count += 1
    else:
        if val != theID:
            count -= 1
        else:
            count += 1
print (theID)
```
