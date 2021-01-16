# # 读取人物名称
# f1 = open('name.txt','r', encoding='UTF-8')
# date = f1.read()
# date.split('|') # 数据分割，用|分割文件中的内容
# print(date.split('|'))
# f1.close()
#
# # 读取兵器名称
# f2 = open('weapon.txt','r', encoding='UTF-8')
# # date = f2.read()
# i = 1
# for line in f2.readlines():          # 冒号！！！！
#     if  i % 2 == 1:                 # 冒号！！！！
#         print(line.strip('\n'))         # 文本本身每一行会有换行符，此处如果不删除，还会输出空行
#     i += 1
# f2.close()

# # 用函数计数
# import re                           # 调用库
# def find( hero ):                   # 创建函数
#     with open('sanguo.txt','r', encoding='UTF-8') as y:
#         date = y.read().replace('\n', '')               # 用无取代换行符
#         num = len(re.findall(hero, date))               # re.findall读取一个记录一个，因此取长度
#     return num
#
# name_num = {}
# with open('name.txt','r', encoding='UTF-8') as x:
#     for line in x:
#         lines = line.split('|')
#     for name in lines:
#         n = find(name)
#         name_num[name] = n
#
# weapon_num = {}
# with open('weapon.txt','r', encoding='UTF-8') as x:
#     lines = []
#     i = 1
#     for line in x.readlines():
#         if i % 2 == 1:
#           item = line.strip('\n')
#           lines.append(item)
#         i += 1
#
#     for weapon in lines:
#         n = find(weapon)
#         weapon_num[weapon] = n
#
# print(name_num)
# print(weapon_num)

# 函数的可变长参数
def func1(first, second):               # 冒号！！！
    print(first + second)

# func1(1,2)             # 定义的两个参数是必须参数，如果不进行输入会报错


def func2(first, *second):
    obj= {}
    for key in second:
        print(key)
    # print(len(first) + len(second[0])-len(second[1]))

func2('123','1','2')