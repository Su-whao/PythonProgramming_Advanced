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



class User:
    def __init__(self, birthday):
        # 双下划线不能通过.直接访问
        self.__birthday = birthday

    def get_age(self):
        return 2018 - self.__birthday.year


if __name__ == "__main__":
    user = User(Date(1990,2,1))
    print(user.get_age())
    # print(user.__birthday) # 报错，不能直接访问
    print(user._User__birthday) # 本质上加双下划线是改变了变量名：_classname__varname

