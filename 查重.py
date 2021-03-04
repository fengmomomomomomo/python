import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# with open('D:\\D\\研究生\\导助\\2021校友卡邮寄信息统计.xlsx', encoding='unicode_escape') as date1:
#     with open('D:\\D\\研究生\\导助\\校友卡名单统计.xlsx', encoding='unicode_escape') as date2:
#         print(date1.read())
#         print(date2.read())

date1 = pd.DataFrame(pd.read_excel('D:\\D\\研究生\\导助\\2021校友卡邮寄信息统计.xlsx'))
date2 = pd.DataFrame(pd.read_excel('D:\\D\\研究生\\导助\\校友卡邮寄.xls'))
# print(date1)
# print(date2)
# print(date1)
# print(str(date2.loc[1, ['学号']]))

# print(len(date2['学号']))
# print(date1.loc[0,'学号'])
#  1. isin 求 1和2都有的学号
#  2. ~ 取反
#  3. 重新给 index
# date2= date2[~date2['学号'].isin(date1['学号'])]
# +
# # date2= date1[~date2['学号'].isin(date1['学号'])]
# = u want
# # date2.index= range(0, len(date2))
# # print(date2)
# pd.concat() 合并两个

date3 = pd.DataFrame()
for i in range(len(date2['学号'])):
#     has = 0
#     for j in range(len(date1['学号'])):
#         if date2.loc[i, '学号'] == date1.loc[j, '学号']:
#            has = 1
#     if has == 0:
#         date3 = date3.append(pd.Series(date2.loc[i], name= date3.shape[0] + 1))
# print(date3)

    if date2.loc[i, '学号'] not in list(date1['学号']):   #dataframe格式提取单元格值或行只能用loc
                                                      # 提取列或行后是series格式，要转化为list
        # print(date2.loc[i, '学号'])
        # print(date1['学号'])
        date3 = date3.append(date2.loc[i])
        # print(pd.Series(date2.loc[i]))
        # print((date2.loc[i]))
        # print(type(pd.Series(date2.loc[i])))
        # print(type(date2.loc[i]))
print(date3.reset_index())