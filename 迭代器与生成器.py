










# a = ['a','d','g']
# b = lambda x: a[1]
# print(b(a))


# a = [1,2,3]
# b = map(lambda x:x+1, a)
# print(list(b))

# a=[1,2,3,4,5]
# b = filter(lambda x:x<=3,a)
# print(list(b))

a=[1,2,3,4]
b=[4,5,6,7]
from functools import reduce
b = reduce(lambda x,y:x+y,a,0)
print(b)