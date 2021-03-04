class Player():
    def __init__(self,name,hp):
        self.__name = name              # 加上__会使名字无法直接被覆盖，类的封装
        self.hp = hp
    def Player_print(self):
        print("%s:%d" %(self.__name,self.hp))
    def newName(self,newName):                   # 需要通过函数重新重新赋值
        self.__name = newName


class Monsters():
    def __init__(self,hp=100):
        self.hp = hp
    def run(self):
        print('keyipao')

class   Boss(Monsters):
    def dance(self):
        print('haihuitiaowu')


a = Boss
print(a.)

# u1 = Player('a',100)
# u2 = Player('b',50)
# u1.Player_print()
# u2.Player_print()
#
# u2.__name = 'c'                             # 无法直接覆盖原名称
# u2.Player_print()
#
# u2.newName('c')                                 # 需要调用函数
#
# u2.Player_print()
