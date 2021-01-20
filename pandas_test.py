import pandas as pd

# s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
# print(s1)
#
# print(s1['a'])
#
#
# s1['a'] = 6
# print(s1['a'])
#
sdate = {'s':5,'d':7,'r':9}
s2 = pd.Series(sdate)
print(type(s2.index[1]))
# print(s2)
# s2.index = ['a','b','c']                    # index函数无法直接添加新变量，只有reindex可以
# print(s2)
# s3 = s2.reindex(['a','b','c','e'])          # 此处要赋值给新变量，否则无法直接添加e
# print(s3)
# s22 = pd.Series(['blue', 'purple', 'yellow'], index = [0, 2, 4])
# s33 = s22.reindex(range(7), method='ffill')          # ffill用来给空变量赋前一个变量的值
s3 = s2.reindex(range(5))
s3[0:5] = ['a','b','c','d','e']
print(s3.reindex(index=range(7), method='ffill'))

# s3 = s2.reindex(range(7), method='bfill')          # fill_value用来给空变量赋后一个变量的值
# print(s3)

# date = {'city':['shanghai','guangzhou','shenzheng','beijing'],
#         'year':[2016,2017,2018,2019],
#         'pop':[1.5,2.7,3.4,5.5]}

# frame = pd.DataFrame(date , columns=['city','year','pop'])
# print(frame)
#
#
# pop = {'beijing':{2018:100,2019:90},
#        'shanghai':{2018:70,2019:40}}
# frame1 = pd.DataFrame(pop)
# print(frame1)
# print(frame1.T)