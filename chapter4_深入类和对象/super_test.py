class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

# 既然已经重写了子类的__init__ 为什么还要执行父类的__init__呢？
# super的执行顺序是什么？

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()

if __name__ == "__main__":
    print(D.__mro__)
    d = D()