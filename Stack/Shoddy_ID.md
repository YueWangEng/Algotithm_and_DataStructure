### Problem Description: Searching Shoddy ID
There is a sequence of IDs，in which the repetive rated of one shoddy ID is higher the 50%. Please find the shoddy ID.

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
