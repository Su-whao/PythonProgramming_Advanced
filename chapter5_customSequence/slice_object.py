import numbers

class Group:
    # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    # 实现切片关键
    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])


    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    # in 语句魔法函数
    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

staffs = ['bobby1', 'imocc', 'bob2', 'bob3']
group = Group(company_name = "imooc", group_name="user", staffs=staffs)
subGroup = group[:2]
print(subGroup)

print(len(group))

if 'bobby1' in group:
    print('yes')

reversed(group)
print(group.staffs)