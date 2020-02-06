# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-09 15:50:18
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-09 23:29:42
 * @Description: None
'''



class User:
    # new是用来控制对象的生成过程，在对象生成之前
    # 可以接收到实例化时的参数
    def __new__(cls, *args, **kwargs):
        print('in new')
        return super().__new__(cls)
    # init是用来完善对象的，是对new返回的对象执行的操作
    # 如果new方法不返回对象则init不执行
    def __init__(self, name):
        print('in init')
        self.name = name

if __name__ == '__main__':
    user = User('wanghao')