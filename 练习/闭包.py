# def counter(x):
#     a = [x]
#     def num():            # 函数里头套函数，是闭包
#         a[0] += 1
#         return a[0]
#     return num            # 此处返回函数名，不带括号
#
# test1 = counter(1)        # 此处输入x的值
# print(test1())
#
# print(test1())
#
# print(test1())

# def line(a, b):
#     def x(x):
#         return a*x+b
#     return x
#
# line1=line(2,4)
# print(line1(5))             # 此处输入闭包中第二个函数的值
#
#


def zhuangshiqi(func):
    def line(a, b):
        print(2 * func(a, b) + 4)

    return line


@zhuangshiqi
def test(a, b):
    return a + b


test(1, 2)
