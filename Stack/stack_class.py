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
