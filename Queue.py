class Queue:
    def __init__(self,length):
        self.queue = [0 for _ in range(length)]
        self.front = 0
        self.rear = 0   #初始化，此时，queue为空
        self.length = length

    def push(self,v):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.length
            self.queue[self.rear] = v
        else:
            raise IndexError('The queue is filled')

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.length    #此处设计的queue,front所指位置总是为零，front的下一个位置才是queue的起始位置。这样设计易于判断queue是否已满。
            return self.queue[self.front]
        else:
            raise IndexError('The queue is empty')
    
    def is_empty(self):
        return self.front == self.rear  #可直接return条件语句，判断结果，返回True或者False
    
    def is_filled(self):
        return (self.rear + 1) % self.length == self.front

q = Queue(5)
l = [i for i in range(3)]
for i in l:
    q.push(i)

print(q.pop())
print(q.pop())
