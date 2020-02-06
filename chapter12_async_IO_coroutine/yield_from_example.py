# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-11 20:29:17
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-12 09:31:09
 * @Description: None
'''

final_result = {}

def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name+"销量：", x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums
    

def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key + "销量统计完成！！") 

def main():
    data_set = {
        "wh牌面膜": [1200, 1500, 3000],
        "wh牌手机": [28, 55, 98, 108],
        "wh牌大衣": [280, 560, 778, 70]
    }

    for key, data_set in  data_set.items():
        print("start key:", key)
        m = middle(key)
        m.send(None)

        for value in data_set:
            m.send(value)
        m.send(None)
    print("final_result:", final_result)

main()