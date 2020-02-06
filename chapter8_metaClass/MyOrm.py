# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-09 23:58:47
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-10 11:57:49
 * @Description: None
'''

import numbers

# 需求
# 通过元类方式实现数据库ORM
# 创建类时会通过元类 metaclass 类来进行创建前的操作，进行类的舒适化操作
# 通过实现__get__  __set__  __delete__魔法函数来实现一个数据描述符


class Field:
    pass

class IntField(Field):
    # 数据描述符
    def __init__(self, db_column, min_value=None, max_value=None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_cloumn = db_column
        
        if not min_value is None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError("min_value must be int")
            elif min_value < 0:
                raise ValueError("min_valule muse be positive int")

        if not max_value is None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError("min_value must be int")
            elif min_value < 0:
                raise ValueError("min_valule muse be positive int")
        if min_value is not None and max_value is not None:
            if max_value < min_value:
                raise ValueError("min_value musr  smaller than max_value")

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("Int value is need")
        if not self.min_value:
            if value < self.min_value:
                raise ValueError("value must bigger than min_value")
            if not self.max_value:
                if value > self.max_value:
                    raise ValueError('value musr smaller than max_value')

        self._value = value

class CharField(Field):
    def __init__(self, db_column, max_length=None):
        self._value = None
        self.db_cloumn = db_column
        if max_length is None:
            raise ValueError("you musr spcify max_length for CharField")
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("String value is need")
        if not self.max_length and len(value) > self.max_length:
            raise ValueError("String length excess max_length")
        self._value = value

class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        # BaseModel 也会执行这个元类，但是他不需要进行如下设置，甚至没有Meta属性，所以单独判断，跳过。
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs, **kwargs)
        fields = {}
        for key , value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
        attrs_meta = attrs.get('Meta', None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, 'db_table', None)
            if table is not None:
                db_table = table
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]
        
        # 这里 attrs 里面的属性就直接传到类实例化的self里面
        return super().__new__(cls, name, bases, attrs, **kwargs)

class BaseModel(metaclass=ModelMetaClass):
    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return super().__init__()

    def save(self):
        # 在这里可以拼 sql 语句
        fields = []
        values = []
        for key, value in self.fields.items():
            db_column = value.db_cloumn
            if db_column is None:
                db_column = key.lower()
            fields.append(db_column)
            value = getattr(self, key)
            values.append(str(value)) # 年龄字段是数字类型，这里转为字符串在sql语句拼装时需要字符串，否则报错。
        # 如果插入字符串的画，本身需要拼装一个引号
        sql = "inset {db_table} ({fields}) value({values})".format(db_table=self._meta["db_table"], fields=",".join(fields), values=",".join(values))
        
        # 接下来通过mysql引擎将数据添加到数据库中
        pass

# 这里会查找到父类的metaclass
class User(BaseModel):
    name = CharField(db_column="name", max_length=10)
    age = IntField(db_column="age", min_value=0, max_value=100)



    class Meta:
        db_table = "user"


if __name__ == '__main__':
    user = User()
    user.name = 'wanghao'
    user.age = 18
    # print(user.fields) # 可以直接取到fields属性
    user.save()