# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-10 13:54:55
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-10 14:07:52
 * @Description: 读大文件
'''


# 读一个大文件，500G，但是只有一行，以特殊的行分割符 {|} 来标识每一行

def myreadlines(f, newline):
    '''
    :f 文件
    : newline 行分割符
    '''
    buf = ""
    while True:
        # 判断buf中是否存在行分割符
        while newline in buf:
            pos = buf.index(newline)
            # 返回buf中行分割符以前的内容
            yield buf[:pos]
            # 将buf'更新为第一个分割符之后的内容，然后再次循环判断
            buf = buf[pos + len(newline):]
        # 当前buf中已经没有分割符了，进行下一次读取
        chunk = f.read(4096*10)
        # 最后一行可能没有行分隔符，直接返回
        if not chunk:
            # 已经读到了文件结尾
            yield buf
            break
        buf += chunk


with open("./迭代器和生成器/bigfile.txt") as f:
    for line in myreadlines(f, '{|}'):
        print(line)