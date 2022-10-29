# Tips for coding

### 1) 创建列表  
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

### 2) 不反复调用的简单函数，尽量使用匿名函数lambda  
```
x = lambda args: expression
```

### 3) 迭代指令  
灵活使用`while...else`和`for...else`，没有中断语句。
例如break,return,则执行else后面的语句

### 4) 常用的辅助函数  
`zip()`, `map()`, `sort()`

### 5) 类型转化函数，用于转化序列为相应的类型，list(), dict(), set()，其中set()可用于去重。

### 6) divmod(x,y)函数，可以同时返回整数商和余数

### 7) set的效率更高，速度快. 
例如，查找效率：set>dict>list,时间复杂度set为o(log(n))，list为o(n).

### 8) 字典三序列  
`dic.keys()`, `dic.values()`, `dic.items()`，返回值均为序列，需要列表形式，则用`list()`转换

### 9) 排序函数
`sort()`（仅针对list）, `sorted()`, `max()`, `min()`, 要会用key参数解决问题。

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
### 12) 逆向提取序列中的元素，可以使用-1参数，  
例如对于列表l中，`l[5:1:-1]`是对于位置5到位置2的元素逆序,
也可用遍历`for i in range(5,1,-1)`实现。

### 13）处理字符串，特别是长句，常用函数
`join()`
`filter()`
`replace()`
`rstrip(arg)`
`split(arg)`

### 14) input函数  
输入字符串: `inp = input('please input a string: ')`  
输入数字: `inp = int(input('please input a number: '))`  
输入列表: `inp = list(map(int,input().rstrip().split()))`  