# Tips for coding

### 1 创建列表  
```
list = [i for i in range(10)]
list = [0 for _ in range(10)]
list1 = [0]*10
```
还可在列表中对每个元素进行简单处理，相当于`map()`函数，例如,  
```
list1 = [i+2 for i in list]
list1 = [str(i) for i in list]
list1 = [str(i) for i in range(10)]
```

### 2 不反复调用的简单函数，尽量使用匿名函数lambda  
```
x = lambda args: expression
```

### 3 迭代指令  
灵活使用`while...else`和`for...else`，没有中断语句，例如break,return,则执行else后面的语句

### 4 常用的辅助函数  
`zip()` `map()`，这两个函数返回值均为迭代器。需要列表形式，则用`list()`转换。

其中，`zip()`用于一一对照。例如：  
```
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = zip(x, y, z)
u = zip(*xyz)
```

### 5 类型转化函数  
用于转化序列为相应的类型，`list()`, `dict()`, `set()`，其中`set()`可用于去重。  

### 6 数字处理
按位提取各位数字:  
  (1) 先转化为string，string为序列，可按位读取，`list_n = [int(i) for i in str(n)]`。  
  (2) 采用商余函数 `divmod(x,y)`，可以同时返回整数商和余数。  
  ```
  list = []
  while n > 0:
    n, y = divmod(n, 10)
    list.append(y)
  ```

### 7) set的效率更高，速度快. 
例如，查找效率：set > dict > list,时间复杂度set为o(log(n))，list为o(n).

### 8) 字典三序列  
`dic.keys()`, `dic.values()`, `dic.items()`，返回值均为迭代器。需要列表形式，则用`list()`转换。

### 9) 排序函数，要会用key参数解决问题。
`sort()`（仅针对list），对现有list直接排序，`list.sort(key, reverse)`。没有返回值。  

`sorted()`, 系统函数，可用于所有可迭代对象，包括字符串, sorted(iterable, key, reverse)。返回值为一个新的list。  
  key function作为定制排序规则，reverse默认为False，即升序。  
 
`max()`, `min()`，系统函数，可用于所有可迭代对象，包括字符串。返回值为最值。  

### 10) 递归函数  
由于要递归题目提供的实例构造方法，需使用`self.方法(参数)`形式。  
递归函数：1）需要终止条件；2）只关注本层任务；3）返回结果只需关注最终结果。

### 11) “列表 += 元组”，是可行的。
```
l = [1,2,3,4,5]
t= (6,7,8,9,10)
l += t
print(l)
```

### 12) 序列的反转处理
以下为序列的反转方法（数字不是序列，字符串属于序列）:

1) 使用-1参数反向读取，`squ_r = squ[::-1]`。例如对于列表ll中，`ll[5:1:-1]`是对于位置5到位置2的元素逆序，也可用遍历`for i in range(5,1,-1)`实现。  
2) 内置函数 reversed()，该函数只是读取，如 `for value in reversed (ll)` 可用于反向读取ll中的项。但该函数不会更改原值，且返回值只为数据类型。若要获取反转后的序列，需用 `squ_r = ''.join(reversed(squ)`。  
3) list内置函数，`list.reverse()`,只适合于list。  
4) 自定义数字反转函数。按位提取，反向获得反转数字。  

### 13）处理字符串，特别是长句，常用函数
`join()`  
`filter()`  
`replace()`  
`rstrip(arg)`  
`split(arg)`  
`正则表达式`

### 14) input函数  
输入字符串: `inp = input('please input a string: ')`  
输入数字: `inp = int(input('please input a number: '))`  
输入列表: `inp = list(map(int,input().rstrip().split()))`  

### 15) 链表问题
常用方法：1）递归；2）设置虚拟头节点；3）快慢指针；4）测试函数（链表和列表之间互相转换）。

### 16) 序列的解开处理
列表、元组前面加星号作用是将列表解开成多个独立的参数，传入函数。例如:  
```
def add(a, b):
    return a + b
data = [7, 8]
print(add(*data))
```
字典前面加两个星号，是将字典解开成为独立的元素作为形参。

### 17）随机变量
采用random模块可生成各种形式的随机变量。例如：

在一定范围内生成随机整数：   
```
import random
hh=random.randint(100,150)
print(hh)
```
在一定范围内生成一定长度的随机整数列表：  
```
ll = random.choices([i for i in range(100)],k=3)
print(ll)
```

### 18) 正则表达式之提取字符串（括号，任意两个指定字符之间等等）。
例如提取(}之间的字符串，返回满足条件的字符串的列表。
```python3
import re
str = '1n3(dfngj}redfk'
p1 = re.compile(r'[(](.*?)[}]', re.S)
ll = re.findall(p1, str)
print (ll)
```
### 19) 函数的定义必须在函数的调用之前。但函数A内部调用另一个函数B，则函数B的定义可以在函数A之后。

### 20) 字符串的大小比较。
在python中，默认是按照ascii的大小比较的；  
字符串按位比较，两个字符串第一位字符的ascii码谁大，字符串就大，不再比较后面的；第一个字符相同就比第二个字符串，以此类推。
例如：`'f' > 'abc'`. 
