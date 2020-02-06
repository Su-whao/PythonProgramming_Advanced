# try except else finally

def exe_try():
    try:
        filepath = ''
        f = open(filepath)
        print("code started")
        raise KeyError
    except KeyError as e:
        print("key error")
    except IndexError as e:
        print("Index error")
    else: # 没有异常时运行 
        print("Not error")
    finally:
        print("Finally")
        f.close()

def exe_try2():
    try:    
        print("code started")
        raise KeyError
        return 1
    except KeyError as e:
        print("key error")
        return 2
    else: # 没有异常时运行 
        print("Not error")
        return 3
    finally:
        # 此时仍然会执行完finally才去return 2或4
        print("Finally")
        # return 4

# 上下文管理器
# __enter__   __exit__ 两个魔法函数
class Sample():
    def __enter__(self):
        # 获取资源
        print("enter")
        return self
    def __exit__(self, exe_type, exe_val, exe_tb):
        # 释放资源
        print("exit", exe_type, exe_val, exe_tb)
    def do_somethind(self):
        print("do something")

if __name__ == "__main__":
    # result = exe_try2()
    # print(result)

    with Sample() as sample:
        sample.do_somethind()