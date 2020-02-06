class A:
    # 类变量，所有实例共享
    aa = 1

    def __init__(self, x, y):
        # self是实例
        # x y 是实例变量
        self.x = x
        self.y = y


a = A(2,3)
print(a.x ,a.y, a.aa)
print(A.aa)
A.aa = 11
a.aa = 111
print(a.aa) # 11
print(A.aa)
# print(A.x) # 报错，A没有x这个属性