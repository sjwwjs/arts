## Python小技巧

- 装饰器：当我们想要为某个函数临时添加某个功能时，装饰器能很好地完成这项工作。
==装饰器其实就是在函数里定义函数：将目标函数对象传入装饰器里，装饰器内部的函数做一些事情，然后再执行目标函数。==

```
def decorator(func):
    def wrapper(*args, **kwargs):
        print('hello')
        return func(*args, **kwargs)
    return wrapper

@decorator
def test(text):
    print(text)

test('这是关于装饰器的测试')
# 输出：
# hello
# 这是关于装饰器的测试
```
- 这里的@是python的语法糖，==作用相当于test = decorator(test)，即把目标函数对象传入装饰器中。由于decorator返回的是函数对象wrapper，原来的test便转而指向了wrapper。当我们调用test时，实际上是调用了wrapper。==
有时我们需要给装饰器传参，这就麻烦一点，需要多定义层函数：

```
def log(context='hello'):
    def decorator(func):
        def warpper(*args, **kwargs):
            print(context)
            return func(*args, **kwargs)
        return warpper
    return decorator

@log(context='hi')
def test(text):
    print(text)

test('这是关于装饰器的测试')
# 输出：
# hi
# 这是关于装饰器的测试
```
- 这里要注意，由于此时的装饰器log有默认参数，所以必须以@log()的形式进行装饰。如果还是用@log，相当于test = log(test)，这就把test赋给了context而decorator缺少位置参数func。而用@log()则使test指向decorator。



---
- 常用的内置装饰器
- @property装饰器可以把类的方法变成属性

```
class Student():
    def __init__(self,score):
        self.score = score

#调用Student类
qiuyue = Student(90)
print(qiuyue.score) #输出结果90
```
- 可是这样也不无问题，比如当输入分数不合理（如1000）时，无法对分数进行检查。当然，可以对Student类附加方法实现检查分数。

```
class Student():
    def get_score(self):
        return self._score

    def set_score(self,value):
        if not isinstance(score,int):
            raise ValueError('score must is an integer!')
        if value > 100 or value < 0:
            raise ValueError('score must between 0 to 100!')
        self._score = value

#调用Student类
qiuyue = Student()
qiuyue.set_score(90)
print(qiuyue.get_score()) #输出90        
```
- 通过set方法对Student的score属性赋值，再用get方法获取score属性。这样就可以实现对score合法性的检查。但是为了一个属性特地写两个方法未免过于繁琐。所以用到装饰器@property封装set方法和get方法，实现对score属性赋值的同时进行数值合法性检查。


```
class Student():
    @property
    def score(self)
        return self._score

    @score.setter
    def score(self,value)
        if not isinstance(value,int):
            raise ValueError('score must is an integer!')
        if value > 100 or value < 0:
            raise ValueError('score must between 0 to 100!')    
        self._score = value

    @property
    def grade(self):
        if self._score is None:
            return None
        elif self._score >= 90:
            print('优秀！')
        elif self._score >=60:
            print('及格！)
        else:
            print('不及格！')

#调用Student类
qiuyue = Student()
qiuyue.score = 90
print(qiuyue.score) # 输出90
qiuyue.score = 1000 # 报错，ValueError
qiuyue.grade = '及格' # 报错
qiuyue.grade # 输出优秀
```
- ==可以看到，@property装饰的第一个score，实际上是一个get方法，而@score.setter装饰的第二个score实际上是set方法。@score.setter其实是@property装饰器的副产品。这两个装饰器一个装饰get方法，一个装饰set方法，这样就使score方法变成了Student类的属性，在对score属性赋值（即set方法）时会自动对值的合法性进行检查，调用score属性即调用get方法。
@grade.setter并不是必须的，当缺少@grade.setter装饰器时grade属性变成只读属性，无法对其进行赋值，只能读取。==

- @classmethod与@staticmethod
- @classmethod

当类中有些方法不需要涉及实例，而需要涉及类，如对类属性的修改，往往使用@classmethod。用@classmethod修饰的方法不会将实例传入方法中，而会自动将自身类作为第一个参数传入。所以这个方法不需要写self参数，但需要一个cls参数代表这个类。


```
class Apple():
    species = '富士苹果'
    @classmethod
    def clsmed(cls):
        print('苹果的种类为：%s' % cls.species)

Apple.clsmed() # 输出：苹果的种类为：富士苹果
```


- @staticmethod

如果类中有些方法既不涉及类，也不涉及实例，可以用@staticmethod。@staticmethod既不会将实例传入方法，也不会将自身类传入方法。所以既没有self参数也没有cls参数。


```
class Apple():
    apple = 1
    def change(self,data):
        self.apple = data
        print('还有%s个苹果' % self.apple)

    @staticmethod
    def stamed():
        print('没有苹果了')

apple = Apple()
apple.change(2) # 输出：还有2个苹果
Apple.stamed() # 输出： 没有苹果了
```
- 下面这个例子加深区分：

```
class Apple():
    species = '富士苹果'
    def __init__(self,data):
        self.num = data

    def common(self):
        print('还有%s个苹果' % self.num)

    @classmethod
    def clsmed(cls):
        print('苹果的种类为：%s' % cls.num)

    @staticmethod
    def stamed():
        print('没有苹果了')

apple = Apple(2)
apple.common() # 输出：还有2个苹果
Apple.clsmed() # 输出：苹果的种类为：富士苹果
Apple.stamed() # 输出：没有苹果了

```
