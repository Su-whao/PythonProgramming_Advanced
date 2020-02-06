
## 2. type, object, class关系

```python
type(1)
# <class 'int'>

type(int)
# <class 'type'>
```
```python
class Student:
    pass
    
stu = Student()
type(stu)
# <class '__main__.Student'>
type(Student)
# <class 'type'>

Student.__bases__
# (<class 'object'>,)
```

type -> int -> 1  
type -> class -> object  

类是由`type`生成的，`object`是所有类的一个基类。  
`type`本身也是一个类，同时也是一个对象。`type`的基类的object。

```python
type(object)
# <class 'type'>

type.__bases__
# (<class 'object'>,)

object.__bases__
# ()

type(type)
# <class 'type'>
```

## 3. python中常见内置类型 

对象三个特征：身份（地址）、类型、值

`None` 对象是唯一的
```
a=None
b=None
id(a) == id(b)
# True
```

- 数值：int, float, complex, bool
- 迭代类型：可以用`for`来遍历
- 序列类型：list, bytes/bytearray/memoryview(二进制序列), range, tuple, str, array
- 映射类型：dict
- 集合：set, frozenset
- 上下文管理类型：with
- 其他：模块, class和实例, 函数类型, 方法类型, 代码类型, object对象, type类型, ellipsis（省略号）类型, notimplemented类型