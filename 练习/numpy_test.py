# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import numpy as np

#
# arr1 = np.array([[1,2,3],[2,3,4]])
# print( arr1)
# print( arr1.dtype)
#
# arr2 = np.array([1.2,2.4,3.6])
# print( arr2)
# print( arr2.dtype)
#
#
# print( arr2 +  arr1)
#
# print(np.zeros((3,5)))
#
# arr3 = np.arange(10)
# print(arr3)
# print(arr3[5])
# print(arr3[5:8])
# arr3[5:8] = 6
# print(arr3)
#
# arr4 = arr3.copy()


# a = np.array([[1,2,3],[4,5,6]])
# print(a.dtype)      # 多维数组的type也是元素的type，而不是一列数据的
# print(a.shape)      #先表示多少行，在表示多少列

#
# persontype = np.dtype({'names': ['name', 'age', 'chinese', 'math', 'english'],
#                        'formats': ['S32', 'i', 'i', 'i', 'f']})
# person = np.array([('liming', 23, 90, 88, 78.5),
#                    ('xiaohua', 24, 80, 78, 90.8),
#                    ('hanmeimei', 73, 87, 93, 90.5)], dtype=persontype)
# ages = person[:]['age']             # 提取出一列单独成列表
# chineses = person[:]['chinese']
# math = person[:]['math']
# english = person[:]['english']
# print(np.mean(ages))
# print(ages)


persontype = np.dtype({'names': ['name', 'chinese', 'english', 'math'],         #dtype创建新格式
                       'formats': ['U25', 'i', 'i', 'i']})  # U25表示中文字符串
person = np.array([('张飞', 66, 65, 30), ('关羽', 95, 85, 98),
                   ('赵云', 93, 92, 96), ('黄忠', 90, 88, 77),
                   ('典韦', 80, 90, 90)], dtype=persontype)               #dtype设置数组格式
names = person[:]['name']               #[:]表示从头到尾,不加也行
chineses = person[:]['chinese']
chineses1 = person['chinese']
englishs = person[:]['english']
maths = person[:]['math']


def tongji(subject, chengji):
    print('{} | {} | {} | {} | {} | {}'
          .format(subject, np.mean(chengji), np.amax(chengji), np.amin(chengji), np.var(chengji), np.std(chengji)))
    # format可以代替%s，返回参数给{}


print('科目 | 平均分 | 最高分 | 最低分 | 方差 | 标准差')
tongji('语文', chineses)
tongji('英语', englishs)
tongji('数学', maths)

range = sorted(person, key=lambda x: x[1] + x[2] + x[3], reverse=True)  # key是排序依据，reverse是排序，=true表示降序
print(range)
