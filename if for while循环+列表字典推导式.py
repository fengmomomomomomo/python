# # 学习if、for、while语句

# # if基本语句
# x = "1234"
# if x == "123":        # 两个等号才是判断相等，一个是复制，if条件结尾要加冒号
#     print('x的值与123相等')
# else:
#     print('x与123不相等')

# # for基本语句
# for i in sengxiao_name:
#     print(i)
#
# for j in range(1,13): # 13是到13前的一个数字，即1到12
#     print(j)

# # while基本语句——break
# num = int(input('输入一个值'))
# while True:
#     print('a')
#     num = num + 1
#     if num > 10:
#         break

# # while基本语句——continue
# num = int(input('输入一个值'))
# while True:
#     num = num + 1
#     if num == 10:
#         continue        #continue是跳过下面的程序，执行下一次的循环
#     print(num)
#
#     if num > 12:
#         break

# # 定义字典
# dict1 = {'x': 1, 'y': 2}  # 用冒号赋予变量的值
# print(type(dict1))
# dict1['z'] = 1
# print(dict1)
# print(dict1)

# # 列表推导式——计算偶数的平方
# list_a = []
# for i in range(13):
#     if i % 2 == 0:
#         list_a.append(i*i)
# print(list_a)
#
# #  等同于如下列表推导式
# list_b = [i*i for i in range(13) if i % 2 == 0]
# print(list_b)





# # 申明生肖和星座的变量
sengxiao_name = ('猴鸡狗猪鼠牛虎兔龙蛇马羊')
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
                 u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# # 建立字典
# dict_sengxiao = {}
# for i in sengxiao_name:
#     dict_sengxiao[i] = 0
#
# dict_xingzuo = {}
# for i in zodiac_name:
#     dict_xingzuo[i] = 0
# # 等同于如下字典推导式
dict_sengxiao = {i: 0 for i in sengxiao_name}

dict_xingzuo = {i: 0 for i in zodiac_name}

while True:     # 使得用户可以重复输入年月日
    # # 注意这里要记得缩进，包括在大的while循环里

    # # 用户输入出生年月日
    year = int(input('输入你的出生年份：'))
    if year == 666:
        for each_key in dict_sengxiao.keys():
            print('生肖%s有%d个' % (each_key, dict_sengxiao[each_key]))

        for each_key2 in dict_xingzuo.keys():
            print('星座%s有%d个' % (each_key2, dict_xingzuo[each_key2]))
        break
    str_month = int(input('月份'))
    str_day = int(input('日期'))



    # # 输出用户的生肖和星座
    print('你的生肖是'+sengxiao_name[year%12])       # 用+连接变量
    # print('你的生肖是%s'%(sengxiao_name[year%12]))   # 用%替换变量

    for num in range(len(zodiac_days)):        #冒号！！！！！！！
        if zodiac_days[num] >= (str_month, str_day):        #冒号！！！！！
            print('你的星座是：%s'%(zodiac_name[num]))
            break
        elif str_month == 12 and str_day > 23:
            print('你的星座是：%s'%(zodiac_name[0]))
            break

    # n = 0
    # while zodiac_days[n] < (str_month, str_day):
    #     if str_month == 12 and str_day > 23:
    #         break
    #     n += 1
    # print("你的星座是：%s"%(zodiac_name[n]))

    dict_sengxiao[sengxiao_name[year%12]] += 1
    dict_xingzuo[zodiac_name[num]] += 1






