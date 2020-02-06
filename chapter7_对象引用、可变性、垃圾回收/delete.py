# python 中垃圾挥手算法是采用 引用计数

a = 1   # 计数 1 的引用1
b = a   # 计数 1 的引用2

del a   # 计数 1 的引用1
# 当引用计数为0，进行垃圾回收

class A:
    # 当Python解释器回收对象的时候执行
    def __del__(self):
        pass

