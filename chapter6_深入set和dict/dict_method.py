a = {
    'bob1' : {"company": 'imooc'},
    'bob2' : {"company": 'imooc'}
}

# a.clear()
# print(a)

new_a = a.copy() # 浅拷贝
new_a['bob1'] = 2   # a没有改变
new_a['bob2']['company'] = 2    # a发生改变


import copy
new_a = copy.deepcopy(a)
new_a['bob1']['company'] = 6

# fromkeys
new_list = ['bobby1', 'bobby2']
new_dict = dict.fromkeys(new_list, {"company": 'imooc'}) # 第一个参数是迭代对象，第二个参数是默认值
print(new_dict)

# get
new_dict.get('bob1', None)

# items
for k,v in new_dict.items():
    print(k,v)

# setdefault
# 没有该key时，将该key和默认的value设置到字典中
default_value = new_dict.setdefault("wanghao", 'imooc')

# update
new_dict.update(bobby1=123, bobby2=234, test=456)
new_dict.update({'bobby1': 'a', 'bobby2': 'b', 'test2': 'test2'})
new_dict.update((('bobby1', 'imooc'), ('bobby2', 2)))
pass