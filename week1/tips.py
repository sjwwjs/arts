平时学习中，记载遇到的一些关于python骚操作。

1：filter()配合匿名函数
首先介绍filter内置函数的作用，过滤器，filter(fun(),[ ])需要两个参数，
第一个为过滤函数，通俗来说就是滤网，第二个就是需要被过滤的对象
例如：需要过滤掉一个列表中小于20的元素，这里为了体现骚，用列表推导式来生成列表

注明：如果不加list()进行强制类型转换，会返回一个对象

2：enumerate([ ],a)枚举器，两个参数第一个为可迭代对象，第二个a为可选参数[start]
所谓枚举，通俗来讲就是按照一定的规则将多方面综合挨个点名

可以把后边2的意思理解为将列表中第一个元素的索引修改为伪索引2，后边的元素依次累加

3：map( )加工厂
map函数也需要两个参数，第一个可以理解为map的返回值，第二个为可迭代对象


4：zip（）匹配器
zip( )函数中可以放无数个可迭代对象 ，实现一一匹配，但是会遵循短板原则，
也就是根据可迭代对象的最短来决定返回值


5.交换字典的键与值。
比如说有：
{‘name':'sam','sex':'male'}  ----> {'sam':name','male':sex'}
dict(zip(dictionary.values(), dictionary.keys()))


6.one-hot编码（机器学习算法相关）
比如对于某数据的Label，希望进行one-hot：
Y = np.zeros((n_sample, n_class), dtype=np.float64)
for k in range(n_class):
      Y[:, k] = y == k
其中n_sample样本的数量，n_class是类别的个数。比如这里n_sample=9,n_class=3。
其中y是label这一列。



7.匿名函数lambda
python里面有一个"懒人专用的函数"，叫做匿名函数(也就是没有函数名)的函数.
我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便.

lambda(这个名字其实是借鉴了另外一个黑客非常喜欢的语言LISP),lambda一般的形式是
关键字lambda 后面跟一个或者多个参数，后面紧跟一个冒号,之后是一个表达式:

lambda arg1,agr2,...agrN:express using arguments

以map()函数为例，若要计算一个列表里面的每个元素的平方，可以直接传入匿名函数：

>>> map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
[1, 4, 9, 16, 25, 36, 49, 64, 81]
通过对比可以看出，匿名函数lambda x: x * x实际上就是：

def f(x):
    return x * x

用匿名函数的好处是显而易见的：

一方面是可以免去取名字的麻烦(因为高质量的代码对函数的取名是有一定的要求的)

而且不必担心函数名冲突

此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
