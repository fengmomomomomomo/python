# 将小说的主要人物记录在文件中

# file_1 = open('小说人物.txt', 'w')   # 如果不加w，是只读文件（r），加上w才可以写入
# file_1.write('诸葛亮')
# file_1.close()                       # 注意文件打开后一定要关闭
#
# file_1 = open('小说人物.txt', 'a')     # 在原有基础上添加文件里的内容用a，否则会覆盖原内容
# file_1.write('刘备')
# file_1.close()

# file1 = open('小说人物.txt')
# print(file1.readline())
# print('=====')
#
# for line in file1.readlines():      #读取时，指针移动后不会自动返回，即读取过的内容不会再次被读取
#     print(line)
#
# file1.close()

file1 = open('小说人物.txt')
print(file1.readline(4))
print(file1.tell())
print(file1.seek(2))
print(file1.seek())

file1.close()


