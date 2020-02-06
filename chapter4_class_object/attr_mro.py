class A:
    name = 'A'
    def __init__(self):
        self.name = 'obj'

a = A()
# print(a.name)
class E:
    pass

class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B, C):
    pass
print(A.__mro__) # A -> B -> B -> D

class B2(E):
    pass

class A2(B2, C):
    pass

print(A2.__mro__) # A2 -> B2 -> E -> C -> D