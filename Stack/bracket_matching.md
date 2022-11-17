




1) Build stack

```python
class Stack:
  def __init__(self) -> None:
    self.stack = []

  def push(self, v):
    return self.stack.append(v)

  def pop(self):
    return self.stack.pop()
  
  def gettop(self):
    if len(self.stack) > 0:
      return self.stack[-1]
    else:
      return None

  def __str__(self) -> str:
        return self.stack
```

2) Solution part  

```Python
#This question doesn't need create stack class,instead, just using the idea of stack is okay.

s = '[lsdkkf]{>[(afi)]}'
s1 = ''.join([i for i in s if i in '{}[]()'])

print(s1)

def matchBracket(string1):
  match = {'}':'{', ']':'[', ')':'('} #Key points: set up the match dictionary, the element waiting for macthing is set as the key.
  stack1 = Stack()
  for i in string1:
    if i in match.values():
          stack1.push(i)
    elif match[i] == stack1.gettop(): #compare the value in the dictionary with the value of top of stack
          stack1.pop()
    else:
          return False
  if len(stack1.stack) == 0:
        return True
  else:
        return False

if __name__== '__main__':
      if matchBracket (s1):
            print ('correct')
      else:
            print('wrong')
```
