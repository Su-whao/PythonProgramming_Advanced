import bisect
from collections import deque

# 用来处理已排序的序列，用来维持已排序的序列（升序）
# 二分查找
#inter_list = []
inter_list = deque() # 只要是可变的序列类型就可以
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 6)
bisect.insort(inter_list, 4)
bisect.insort(inter_list, 5)
print(inter_list)

print(bisect.bisect(inter_list, 3))