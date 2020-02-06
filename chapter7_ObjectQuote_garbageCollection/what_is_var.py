
# python 中变量和 Java 中本质不一样
# Python 的变量本质上是一个指针

a = [1,2,3]
b=a
b.append(4)
print(a)
print(a is b) # a b 是同一个对象 ，is 判断 id 是否相同
print(id(a), id(b)) # 内存地址相同


a = [1,2,3,4]
b = [1,2,3,4]
print(a is b) # False
print(a == b) # True
print(id(a), id(b))

a = 1
b = 1
print(id(a), id(b)) # 相等
print(a is b)
# 将小整数只生成一份, 所以 a b 代表的1 是同一个 1

a = []
b = []
print(a is b) # False

class People:
    pass

person = People()
print(type(person))
if type(person) is People:
    print('yes')