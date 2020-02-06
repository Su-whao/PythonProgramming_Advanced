# set 集合， frozenset 不可变集合 ，无序 不重复

s = {1,2,3}
fs = frozenset([1,3,6,2,8,4])
# frozenset 可以作为dict的key

# 向set添加数据

s.add('a')
s.update({0,6,5,2,7,4,8}) # 拼装起来
s.pop()
print(s)
s.remove(1) # remove an member
print(s)

# difference 差集

a = {1,2,3}
b = {3,4,5}
print(a.difference(b))  # a-b
print(b.difference(a))  # b-a
print(b-a) # b-a

print(a|b)  # 并
print(a&b)  # 交
print(a-b)  # 差

print({1,2}.issubset(a))  # 是子集
print(1 in a)