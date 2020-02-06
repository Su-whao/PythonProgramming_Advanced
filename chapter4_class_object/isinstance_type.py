class A:
    pass

class B(A):
    pass

b = B()

print(isinstance(b, B)) # True
print(isinstance(b, A)) # True

print(type(b))
print(type(b) is B) # True
# is 判断 id 是否相同，== 判断的是值相等
# type 返回的是 id， 指向的是 B
# isinstance 会根据继承关系去找