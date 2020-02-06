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


if __name__ == "__main__":
    new_day = Date(2020, 2, 1)
    new_day.tomorrow()
    print(new_day)
    

    # 2020/2/2
    date_str = '2020/2/2'
    # 用静态方法完成初始化
    new_day = Date.parse_from_string(date_str)
    print(new_day)

    new_day = Date. from_string(date_str)
    print(new_day)    

    print(Date.valid_str(date_str))