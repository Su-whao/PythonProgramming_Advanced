# 列表推导式
odd_list = [x for x in range(1,21,2)]
print(odd_list)


def handle_item(item):
    return item*item

odd_list = [handle_item(x) for x in range(10)]
print(odd_list)

# 列表生成式性能高于列表操作


## 生成器表达式
odd_gen = (x for x in range(1,21,2))
print(odd_gen)



# 字典推导式
my_dict = {'bob1':22, 'bob2':33, 'bob3':44}
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
reversed_dict = {value:key for key,value in my_dict.items()}
print(reversed_dict)


# 集合推导式
my_set = {key for key,v in my_dict.items()}
print(my_set)