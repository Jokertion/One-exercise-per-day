# __doc__ = "问题：存在一个list，其中每个值都为字典，按照字典的值对当前list中的元素进行排序。"
# output： [dict, dict, dict, ..., dict](排序后的list)

_list = [{"x": "x"}, {"x": "z"}, {"x": "y"}, {"x": "a"}]

print(sorted(_list, key=lambda x: list(x.values())))
