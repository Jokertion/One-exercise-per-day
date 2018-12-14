# __doc__ = """问题：给定一个列表 _list，
# 元素如下所示：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，
# 存在另一个列表select，元素如下：[1, 0, 0, 0, 1, 1, 1, 0, 1, 0]，
# 依次对select中的元素进行遍历，
# 当元素为1的时候，对_list进行尾部追加；为0的时候，删除尾部元素。
# 待追加的列表la中元素如下：[76, 45, 1, 16, 100]"""

_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
select = [1, 0, 0, 0, 1, 1, 1, 0, 1, 0]
la = [76, 45, 18, 16, 100]

n = 0
for s in select:
    if s == 1:
        _list.append(la[n])
        n += 1
    else:
        _list.pop()
print(_list)
