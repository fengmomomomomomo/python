# i = j   # NameError 未申明变量
# print())   # SyntaxError 格式错误，多了一个括号
# a=[1,2]
# print(a[3])     # IndexError 索引错误，列表里没有第3个
#
# a={'a':1,'b':2}
# print(a['c'])     # keyError 关键词错误，字典里没有c这个名称
#
# year = int(input('请输入年份：'))     # ValueError,值的类型错误
#input abc

# a = 123
# a.append()      # AttributeError 属性错误，int类型没有append属性

#
try:
    year = int(input('请输入年份：'))
    year.append()
except ValueError:
    print('年份请输入数字')
except AttributeError:
    print('属性错误')

