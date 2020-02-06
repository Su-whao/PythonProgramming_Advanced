import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print("file open") # __enter__ 操作
    yield {}    # 操作
    print("file end") # __exit__ 操作


with file_open("") as f:
    print("file precessing")
