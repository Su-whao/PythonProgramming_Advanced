# list[start:end:step]

a = [1,2,3,4,5]
# a[::2] = ['a', 'b'] # 赋值时，切片取出的数据长度要和右面长度相等
# print(a)

a[2:3] = ['a', 'b', 'c']
print(a)

a[2:5] = ['slice']
print(a)