
```python
class Company(object):
    def __init__(self, employee_lst):
        self.employee = employee_lst
        
    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

company = Company(["tom", "bob", "jane"])
company1 = company[:2]
print(len(company1))

for em in company:
    print(em)
```


## 2. 魔法函数一览

### 2.1 非数据运算

#### (1) 字符串表示

1. \_\_repr__
2. \_\_str__

#### (2) 集合、序列相关

1. \_\_len__
2. \_\_getitem__
3. \_\_setitem__
4. \_\_delitem__
5. \_\_contains__

#### (3) 迭代相关

1. \_\_iter__
2. \_\_next__

#### (4) 可调用

1. \_\_call__

#### (5) with上下文管理器

1. \_\_enter__
2. \_\_exit__

#### (6) 数值转换

1. \_\_abs__
2. \_\_bool__
3. \_\_int__
4. \_\_float__
5. \_\_hash__
6. \_\_index__

#### (7) 元类相关

1. \_\_new__
2. \_\_init__

#### (8) 属性相关

1. \_\_getattr__, \_\_setattr__
2. \_\_getattribute__, \_\_setattribute__
3. \_\_dir__

#### (9) 属性描述符

1. \_\_get__
2. \_\_set__
3. \_\_delete__

#### (10) 协程

1. \_\_await__
2. \_\_aiter__
3. \_\_aenter__
4. \_\_aexit__

### 2.2 数学运算

#### (1) 一元运算符  

1. \_\_neg__(-负数)
2. \_\_pos__(+正数)
3. \_\_abs__

#### (2) 二元运算符

1. \_\_lt__(<)
2. \_\_le__(<=)
3. \_\_eq__(==)
4. \_\_ne__(!=)
5. \_\_gt__(>)
6. \_\_ge__(>=)

#### (3) 算术运算符

1. \_\_add__ +
2. \_\_sub__ -
3. \_\_mul__ *
4. \_\_truediv__ \
5. \_\_floordiv__ \\\\
6. \_\_mod__ %
7. \_\_divmod__ divmod()
8. \_\_pow__ **或pow()
9. \_\_round__ round()

#### (4) 反向算术运算符

1. \_\_radd__
2. rsub
3. rmul
4. rtruediv
5. rfloordiv
6. rdivmod
7. rpow

#### (5) 增量赋值算术运算符

1. iadd
2. isub
3. imul
4. itruediv
5. ifloordiv
6. ipow

#### (6) 位运算符

1. invert ~
2. lshift <<
3. rshift >>
4. and &
5. or |
6. xor ^

#### (7) 反向位运算符

1. rlshift
2. rrshift
3. rand
4. rxor
5. ror

#### (8) 增量赋值位运算符

1. ilshift
2. irshift
3. iand
4. ixor
5. ior

## 3. 实例

### print

```python
class Company:
    def __init__(self, employee_list):
        self.employee = employee_list
        
    def __str__(self):
        return ",".join(self.employee)
    
    def __repr__(self):
        return ",".join(self.employee)
        
company = Company(['tom', 'bob', 'jone'])

print(company)
company
# tom,bob,jone
# tom,bob,jone
```

`print(x)` 会调用 `print(str(x))`  
`str()` 会调用类的 `__str__` 魔法函数。  

在交互模式下直接通过 `company` 的方式打印变量，郑正常情况下会打印类实例的地址，可以通过实现`__repr__`魔法函数改变输出。


### \_\_add__

```python
class MyVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return MyVector(self.x+other.x, self.y+other.y)
    
    def __str__(self):
        return "x:{}, y:{}".format(self.x ,self.y)
    
first_vec = MyVector(1,2)
second_vec = MyVector(2,3)
print(first_vec+second_vec)
# x:3, y:5
```