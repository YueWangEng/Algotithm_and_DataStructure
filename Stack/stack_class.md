### Build a class of stack
在实际应用中，除非特殊要求，一般不需要创建该类，只需使用该解题思想即可。

```python
class Stack:
  def __init__(self) -> None:
    self.stack = []

  def push(self, v):  #add new element
    return self.stack.append(v)

  def pop(self):  #delete the element of top
    return self.stack.pop()
  
  def gettop(self): #get the element of top
    if len(self.stack) > 0:
      return self.stack[-1]
    else:
      return None

  def __str__(self) -> str: #This funtion used in class to let the system to print the oject directly.
        return self.stack
```
