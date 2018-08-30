# Two Sum
# 给出一个数字列表和一个目标值（target），
# 假设列表中有且仅有两个数相加等于目标值，
# 我们要做的就是找到这两个数，并返回他们的索引值。


#第一种做法：两层循环解决(但是时间效率太低)
def algoithm(self, nums, target):
    result = []
    for i in range(len(nums)):
       for j in range(i+1, len(nums)):
           if nums[i] + nums[j] == target:
               result.append(i)
               result.append(j)
               return result
#第二种就是创造字典，将值与对应的序号意义对应
def algoithm(self, nums, target):
        # 创建字典一，存储输入列表的元素值和对应索引
        num_dict = {nums[i]:i for i in range(len(nums))}
        print(num_dict)
        # 创建另一个字典，存储target-列表中的元素的值
        num_dict2 = {i:target-nums[i] for i in range(len(nums))}
        print(num_dict2)
        # 判断num_r是否是输入列表中的元素，如果是返回索引值，不是则往下进行
        result = []
        for i in range(len(nums)):
            j = num_dict.get(num_dict2.get(i))
            if (j is not None) and (j!=i):
                result = [i,j]
                break
        return result