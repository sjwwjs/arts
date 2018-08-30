Dataframe创建方式

1) 由数组列表组成的字典
data1 = {'four':np.arange(4,9), 'one':range(1,6), 'three':[3,4,5,6,7],'two':range(2,7)}
print('(1) 由列表组成的字典')
print(pd.DataFrame(data1, index=list('abcde')))
print('------------')


2) 由Series组成的字典

data2 = {'four':pd.Series(np.arange(4,9), index=list('abcde')), 
         'one':pd.Series(range(1,6), index=list('abcde')),
         'three':pd.Series((3,4,5,6,7), index=list('abcde')),
         'two':pd.Series(range(2,7), index=list('abcde'))}
print('(2) 由Series组成的字典')
print(pd.DataFrame(data2))
print('------------')

3) 通过二维数组直接创建

data3=np.array([4,1,3,2,5,2,4,3,6,3,5,4,7,4,6,5,8,5,7,6]).reshape(5,4)
print('(3)通过二维数组直接创建')
print(pd.DataFrame(data3, index=list('abcde'), columns=['four', 'one', 'three', 'two']))
print('------------')

4) 由字典组成的列表

data4 = [{'four':4,'one':1,'three':3,'two':2}, {'four':5,'one':2,'three':4,'two':3},
         {'four':6,'one':3,'three':5,'two':4}, {'four':7,'one':4,'three':6,'two':5}, 
        {'four':8,'one':5,'three':7,'two':6}]
print('(4)由字典组成的列表')
print(pd.DataFrame(data4, index=list('abcde')))
print('------------')

5) 由字典组成的字典

data5 = {'four':{'a':4, 'b':5, 'c':6, 'd':7, 'e':8}, 
        'one':{'a':1, 'b':2, 'c':3, 'd':4, 'e':5}, 
        'three':{'a':3, 'b':4, 'c':5, 'd':6, 'e':7}, 
        'two':{'a':2, 'b':3, 'c':4, 'd':5, 'e':6}}
print('(5)由字典组成的字典')
print(pd.DataFrame(data5, index=list('abcde'), columns=['four', 'one', 'three', 'two']))

由以上五种方式都可以创建相同的Dataframe，但主要还是依据当时情况做决定使用最便捷的方式。