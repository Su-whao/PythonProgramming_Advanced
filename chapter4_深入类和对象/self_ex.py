# 自省是通过一定的机制查询到对象的内部结构

class Date:
    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 实例方法
    def tomorrow(self):
        self.day += 1

    # 静态方法，不需要传self参数，调用必须用Date
    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split('/'))
        return Date(int(year), int(month), int(day))
    
    # 类方法
    @classmethod
    def from_string(cls, date_str): # cls传递的是类对象（Date）
        year, month, day = tuple(date_str.split('/'))
        return cls(int(year), int(month), int(day))
    
    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split('/'))
        if  int(year) > 0 and 0 < int(month) <= 12 and 0 < int(day) <= 31:
            return True
        else:
            return False


    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)


class Person:
    '''人'''
    name = "user"

class Student(Person):
    def __init__(self, schoolName):
        self.schoolName = schoolName

if __name__ == "__main__":
    user = Student("慕课网")

    # # 通过__dict__查询属性
    # print(user.__dict__) # name属性没有进入__dict__，因为name是Person的不是studnet实例的
    # print(user.name)
    # print(Person.__dict__)

    # user.__dict__['schoolAddr'] = "太原市"
    # print(user.schoolAddr) # 太原市

    print(dir(user)) # 列出对象所有属性

    a = [1,2]
    print(dir(a))