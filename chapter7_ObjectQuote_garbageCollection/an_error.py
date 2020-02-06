def add(a ,b):
    a += b
    return a

class Company():
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs
    
    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)

if __name__ == "__main__":
    # a = 1
    # b = 2
    # c = add(a,b)
    # print(a,b,c) # a 没收到影响

    # a = [1,2]
    # b = [3,4]
    # c = add(a,b)
    # print(a,b,c) # a 受到影响

    # a = (1,2)
    # b = (3,4)
    # c = add(a,b)
    # print(a,b,c) # a 没受到影响

    com1 = Company('com1', ['bob1', 'bob2', 'bob3'])
    com1.add('bob4')
    com1.remove('bob3')
    print(com1.staffs)

    com2 = Company("com2")
    com2.add('bob')

    com3 = Company("com3")
    com3.add('bob5')
    
    print(com2.staffs)
    print(com3.staffs)
    print(com2.staffs is com3.staffs) # True
    # 因为com2和com3都使用了默认的空列表，实际上是使用了同一个列表