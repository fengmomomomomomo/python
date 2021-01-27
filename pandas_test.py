import pandas as pd
from pandas import Series, DataFrame

# s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
# print(s1)
#
# print(s1['a'])
#
#
# s1['a'] = 6
# print(s1['a'])
# #
# sdate = {'s':5,'d':7,'r':9}
# s2 = pd.Series(sdate)
# print(type(s2.index[1]))
# # print(s2)
# # s2.index = ['a','b','c']                    # index函数无法直接添加新变量，只有reindex可以
# # print(s2)
# # s3 = s2.reindex(['a','b','c','e'])          # 此处要赋值给新变量，否则无法直接添加e
# # print(s3)
# # s22 = pd.Series(['blue', 'purple', 'yellow'], index = [0, 2, 4])
# # s33 = s22.reindex(range(7), method='ffill')          # ffill用来给空变量赋前一个变量的值
# s3 = s2.reindex(range(5))
# s3[0:5] = ['a','b','c','d','e']
# print(s3.reindex(index=range(7), method='ffill'))

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







#
# kaoshi = {'name':['zhangfei', 'guanyv', 'caocao','dianwei'],
#           'chinese':[90,89,88,87],'english':[86,85,84,83],
#           'math':[82,81,80,79]}
# tongji1 = DataFrame(kaoshi)
# tongji2 = DataFrame(kaoshi, index=['zhangfei', 'guanyv', 'caocao', 'dianwei'],
#                    columns=['chinese', 'english', 'math'])
# print




score = DataFrame(pd.read_excel('C:\\Users\\L\\Desktop\\tese1.xlsx'))   # 读取excel表
# print(score)
# score.to_excel('tese1')


score = score.set_index('name')                  # 将指定列设为索引
# score.at['zhangfei', 'math'] = 85                # 修改单个位置的值


# score.isnull()
# print(score.describe())

score = score.drop_duplicates()                                         # 去处重复值
score['math'].fillna(score['math'].mean(), inplace=True)                # 以第一个参数填充空值
score['sum'] = score.sum(axis=1)                                        # axis1为行，对行求和
score.sort_values(by='sum', ascending= False, inplace=True)             # 以by后面的索引排序，默认升序
print(score)
# score.to_excel('C:\\Users\\L\\Desktop\\tese1.xlsx')         # 输出到excel表
