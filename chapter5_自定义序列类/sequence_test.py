# 序列可以用for遍历
# str bytes bytearray array 是扁平序列
# list deque bytearray array 是可变序列
# str tuple bytes 不可变


from collections import abc

a = [1,2]
# c = a + (3,4) # 报错

a += (3,4)  # 不报错，+= 接收的参数可以为任意序列类型
# += 调用 __iadd__ 魔法函数 
# print(a)

a.extend((4,5)) # extend 接收序列类型
print(a)